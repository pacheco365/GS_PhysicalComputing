import cv2
import mediapipe as mp
import math

#MediaPipe
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils


#Função para calcular o ângulo entre três pontos
def calcular_angulo(p1, p2, p3):
    angulo = math.degrees(math.atan2(p3.y - p2.y, p3.x - p2.x) - math.atan2(p1.y - p2.y, p1.x - p2.x))
    return abs(angulo)


#Função para verificar o agachamento
def verificar_agachamento(landmarks):
    #definindo cada parte do corpo
    quadril_esq = landmarks[mp_pose.PoseLandmark.LEFT_HIP]
    quadril_dir = landmarks[mp_pose.PoseLandmark.RIGHT_HIP]
    joelho_esq = landmarks[mp_pose.PoseLandmark.LEFT_KNEE]
    joelho_dir = landmarks[mp_pose.PoseLandmark.RIGHT_KNEE]
    tornoza_esq = landmarks[mp_pose.PoseLandmark.LEFT_ANKLE]
    tornoza_dir = landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE]

    angulo_joelho_esq = calcular_angulo(quadril_esq, joelho_esq, tornoza_esq)
    angulo_joelho_dir = calcular_angulo(quadril_dir, joelho_dir, tornoza_dir)

    #Considera o agachamento como "bem feito" se os joelhos formarem um ângulo abaixo de 90 graus
    agachamento_alto = angulo_joelho_esq > 150 and angulo_joelho_dir > 150

    # Condições para mostrar feedback adequado
    if agachamento_alto:
        feedback = "Agachamento incorreto"
    else:
        feedback = "Agachamento correto"

    return agachamento_alto, feedback


#Função principal para contar repetições e verificar se está correto
def contar_repeticoes(video):
    cap = cv2.VideoCapture(video)
    contador_agachamento = -1
    agachamento_alto_anterior = False

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(frame_rgb)
        if results.pose_landmarks:
            mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
            #Verificando o agachamento
            agachamento_alto, feedback = verificar_agachamento(results.pose_landmarks.landmark)
            if agachamento_alto and not agachamento_alto_anterior:
                contador_agachamento += 1
                print(f"Agachamentos: {contador_agachamento}")
            agachamento_alto_anterior = agachamento_alto
            #Exibindo o feedback visual sobre a execução do agachamento
            cv2.putText(frame, feedback, (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0, 0, 255) if agachamento_alto else (0, 255, 0), 2)
        #resultados
        cv2.putText(frame, f"Contagem: {contador_agachamento}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0),
                    2)
        cv2.imshow("Agachamento - Contagem de Repeticoes", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

video = "VideoGS.mp4"
contar_repeticoes(video)


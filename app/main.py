from app.pipelines.extrair import extrair_excel
from app.pipelines.transformar import concatenar_data_frames
from app.pipelines.load import salva_excel

path = "data/input"

if __name__ == "__main__":
    lista_data_frame = extrair_excel(path)
    data_frame = concatenar_data_frames(lista_data_frame)
    print(salva_excel(data_frame, "data/output", "output"))
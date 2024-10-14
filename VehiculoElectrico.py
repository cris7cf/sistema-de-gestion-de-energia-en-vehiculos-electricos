import matplotlib.pyplot as plt
import math


class VehiculoElectrico:
    def __init__(self, capacidad_bateria_kwh, carga_inicial_kwh):
        self.capacidad_bateria_kwh = capacidad_bateria_kwh
        self.carga_actual_kwh = carga_inicial_kwh
        self.uso_electronicos_kw = 0.5  # Consumo constante de dispositivos electrónicos

    def conducir(self, velocidad_inicial_kmh, velocidad_final_kmh, distancia_km, pendiente_terreno_grados=0,
                 tipo_terreno='pavimento', condiciones_climaticas='soleado', frecuencia_curvas='ninguna',
                 frenada_intensa=False):
        """Simula conducir una distancia con aceleración/desaceleración, pendiente, tipo de terreno, condiciones climáticas, curvas y frenada."""
        energia_consumida = self.calcular_consumo_energia(velocidad_inicial_kmh, velocidad_final_kmh, distancia_km,
                                                          pendiente_terreno_grados, tipo_terreno,
                                                          condiciones_climaticas, frecuencia_curvas, frenada_intensa)
        self.carga_actual_kwh -= energia_consumida
        if self.carga_actual_kwh < 0:
            self.carga_actual_kwh = 0
        return energia_consumida

    def calcular_consumo_energia(self, velocidad_inicial_kmh, velocidad_final_kmh, distancia_km,
                                 pendiente_terreno_grados, tipo_terreno, condiciones_climaticas, frecuencia_curvas,
                                 frenada_intensa):
        """Consumo de energía basado en aceleración, pendiente, terreno, clima, curvas y eficiencia del motor."""

        # Simular aceleración o desaceleración
        delta_v = velocidad_final_kmh - velocidad_inicial_kmh

        # Consumo base de energía por km (kWh/km) ajustado por la eficiencia y aceleración
        consumo_base_energia = 0.2 * (velocidad_final_kmh / 100)  # Modelo simplificado
        if delta_v > 0:
            # Si está acelerando, el consumo es mayor
            consumo_base_energia *= 1.2
        elif delta_v < 0:
            # Si está desacelerando, el consumo es menor
            consumo_base_energia *= 0.8

        # Ajuste por la pendiente del terreno
        factor_pendiente = math.cos(math.radians(pendiente_terreno_grados))
        consumo_energia_terreno = consumo_base_energia / factor_pendiente if factor_pendiente > 0 else float('inf')

        # Simular frenado regenerativo si la pendiente es negativa (descenso)
        energia_regenerada = 0
        if pendiente_terreno_grados < 0 or frenada_intensa:
            energia_regenerada = VehiculoElectrico.calcular_frenado_regenerativo(velocidad_final_kmh, distancia_km,
                                                                                 pendiente_terreno_grados,
                                                                                 frenada_intensa)

        # Ajuste por el tipo de terreno (fricción)
        factor_terreno = VehiculoElectrico.calcular_factor_terreno(tipo_terreno)
        consumo_energia_terreno *= factor_terreno

        # Ajuste por las condiciones climáticas
        factor_clima = VehiculoElectrico.calcular_factor_clima(condiciones_climaticas)
        consumo_energia_terreno *= factor_clima

        # Ajuste por las curvas
        factor_curvas = VehiculoElectrico.calcular_factor_curvas(frecuencia_curvas)
        consumo_energia_terreno *= factor_curvas

        # Consumo total de energía (incluyendo dispositivos electrónicos)
        consumo_total_energia = (consumo_energia_terreno + self.uso_electronicos_kw) * distancia_km

        # Restar la energía regenerada en descensos o frenadas intensas
        consumo_total_energia -= energia_regenerada

        return max(consumo_total_energia, 0)  # No puede ser menor que 0

    @staticmethod
    def calcular_frenado_regenerativo(velocidad_kmh, distancia_km, pendiente_terreno_grados, frenada_intensa=False):
        """Simula la regeneración de energía durante un descenso o frenada intensa."""
        eficiencia_regenerativa = 0.3
        if frenada_intensa:
            eficiencia_regenerativa = 0.5  # Mayor regeneración en frenadas intensas
        energia_regenerada = eficiencia_regenerativa * (0.2 * (velocidad_kmh / 100)) * distancia_km
        return energia_regenerada

    @staticmethod
    def calcular_factor_terreno(tipo_terreno):
        """Ajusta el consumo de energía dependiendo del tipo de terreno (fricción)."""
        factores_terreno = {
            'pavimento': 1.0,  # Terreno estándar
            'grava': 1.2,  # Más fricción, más consumo
            'nieve': 1.5,  # Mucha fricción, más consumo
            'arena': 1.8,  # Terreno muy difícil, alto consumo
        }
        return factores_terreno.get(tipo_terreno, 1.0)  # Default: pavimento

    @staticmethod
    def calcular_factor_clima(condiciones_climaticas):
        """Ajusta el consumo de energía dependiendo de las condiciones climáticas."""
        factores_clima = {
            'soleado': 1.0,  # Clima óptimo
            'lluvia ligera': 1.1,  # Más fricción y resistencia
            'lluvia fuerte': 1.3,  # Mayor fricción y menor adherencia
            'viento a favor': 0.9,  # Menor resistencia del aire
            'viento en contra': 1.2,  # Mayor resistencia del aire
            'nieve ligera': 1.4,  # Mayor fricción por la nieve
            'nieve intensa': 1.6  # Muy difícil, alto consumo
        }
        return factores_clima.get(condiciones_climaticas, 1.0)

    @staticmethod
    def calcular_factor_curvas(frecuencia_curvas):
        """Ajusta el consumo de energía dependiendo de la frecuencia e intensidad de curvas."""
        if frecuencia_curvas == 'ninguna':
            return 1.0
        elif frecuencia_curvas == 'bajas':
            return 1.1  # Pocas curvas, ligero incremento en consumo
        elif frecuencia_curvas == 'moderadas':
            return 1.2  # Curvas moderadas, más fricción
        elif frecuencia_curvas == 'altas':
            return 1.4  # Muchas curvas, alto consumo por pérdida de eficiencia
        return 1.0

    def optimizar_energia(self, velocidad_deseada_kmh, distancia_km, pendiente_terreno_grados=0,
                          tipo_terreno='pavimento', condiciones_climaticas='soleado', frecuencia_curvas='ninguna'):
        """Simula la optimización de energía ajustando la velocidad para minimizar el consumo."""

        # Calcular la velocidad óptima según la pendiente, condiciones y tipo de terreno
        if pendiente_terreno_grados > 5:
            velocidad_optima_kmh = min(50, velocidad_deseada_kmh)  # Velocidades más bajas en pendientes pronunciadas
        elif pendiente_terreno_grados < -5:
            velocidad_optima_kmh = min(80, velocidad_deseada_kmh)  # Velocidades más altas en descensos
        else:
            velocidad_optima_kmh = min(70,
                                       velocidad_deseada_kmh)  # Velocidad óptima en terrenos planos o con poca pendiente

        # Simular conducción con la velocidad óptima
        return self.conducir(velocidad_optima_kmh, velocidad_optima_kmh, distancia_km, pendiente_terreno_grados,
                             tipo_terreno, condiciones_climaticas, frecuencia_curvas)

    def mostrar_bateria(self):
        """Muestra la carga actual de la batería."""
        print(f"Carga actual de la batería: {self.carga_actual_kwh:.2f} kWh")

    def graficar_consumo_energia(self, velocidades_iniciales, velocidades_finales, distancias,
                                 pendiente_terreno_grados=0, tipo_terreno='pavimento', condiciones_climaticas='soleado',
                                 frecuencia_curvas='ninguna'):
        """Visualiza el consumo de energía para diferentes velocidades y distancias."""
        consumo = [
            self.calcular_consumo_energia(vi, vf, d, pendiente_terreno_grados, tipo_terreno, condiciones_climaticas,
                                          frecuencia_curvas, False)
            for vi, vf, d in zip(velocidades_iniciales, velocidades_finales, distancias)]
        plt.plot(velocidades_finales, consumo, marker='o')
        plt.title(f'Consumo de Energía vs Velocidad Final ({tipo_terreno}, {condiciones_climaticas})')
        plt.xlabel('Velocidad Final (km/h)')
        plt.ylabel('Consumo de Energía (kWh)')
        plt.show()


# Ejemplo de uso:
vehiculo = VehiculoElectrico(capacidad_bateria_kwh=75, carga_inicial_kwh=50)

# Simular conducción con aceleración en pavimento y lluvia ligera
energia_consumida = vehiculo.conducir(velocidad_inicial_kmh=60, velocidad_final_kmh=100, distancia_km=10,
                                      pendiente_terreno_grados=5, tipo_terreno='pavimento',
                                      condiciones_climaticas='lluvia ligera', frecuencia_curvas='moderadas',
                                      frenada_intensa=True)
print(f"Energía consumida: {energia_consumida:.2f} kWh")

# Optimizar el uso de energía en una ruta plana con viento en contra y curvas altas
vehiculo.optimizar_energia(velocidad_deseada_kmh=90, distancia_km=20, pendiente_terreno_grados=0,
                           tipo_terreno='pavimento', condiciones_climaticas='viento en contra',
                           frecuencia_curvas='altas')

# Mostrar la carga restante de la batería
vehiculo.mostrar_bateria()

# Graficar consumo de energia
velocidades_iniciales = [60, 65, 75, 80]
velocidades_finales = [85, 90, 95, 100]
distancias = [10, 10, 10, 10]
vehiculo.graficar_consumo_energia(velocidades_iniciales, velocidades_finales,distancias,
                                      pendiente_terreno_grados=5, tipo_terreno='pavimento',
                                      condiciones_climaticas='lluvia ligera', frecuencia_curvas='moderadas')
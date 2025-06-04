export interface TitaticDto {
  Pclass: number;      // Clase del pasajero (1, 2 o 3)
  Sex: number;         // Sexo codificado como número (ej. 0 = mujer, 1 = hombre)
  Age: number;         // Edad en años
  SibSp: number;       // Número de hermanos/esposos a bordo
  Parch: number;       // Número de padres/hijos a bordo
  Fare: number;        // Tarifa pagada
  Embarked: number;    // Puerto de embarque codificado (ej. 0 = S, 1 = C, 2 = Q)

}

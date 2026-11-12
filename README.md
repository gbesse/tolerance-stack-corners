# tolerance-stack-corners

## Français

Comparer tolérances extrêmes et hypothèses statistiques.

Données fictives ; aucun accès réseau ni secret requis.

```sh
python -m tolerance_stack_corners examples/demo.json --lang fr
python -m unittest discover -s tests -v
```

### Méthode et différence

Comparer tolérances extrêmes et hypothèses statistiques : calcul déterministe sur entrées structurées, témoins et cas limites explicites.

### Limites

Modèle borné, données fictives, aucun service ou matériel de production validé. Méthodes classiques ; aucune supériorité SOTA générale ni adoption humaine démontrée.

### Validation

Tests de domaine, cas limites et interface FR/EN/ES. La CI teste Python 3.11/3.13 et exécute la wheel installée hors du checkout. JSON conserve les identifiants techniques et les données fournis. Erreur d’entrée : code de sortie 2.

## English

Compare worst-case tolerances and statistical assumptions.

Synthetic data; no network access or secret required.

```sh
python -m tolerance_stack_corners examples/demo.json --lang en
python -m unittest discover -s tests -v
```

### Method and difference

Compare worst-case tolerances and statistical assumptions: deterministic computation over structured inputs, explicit witnesses and boundary cases.

### Limits

Bounded model and synthetic data; no production service or hardware validated. Classical methods; no general SOTA superiority or human adoption demonstrated.

### Validation

Domain tests, boundary cases and FR/EN/ES interface. CI tests Python 3.11/3.13 and runs the installed wheel outside the checkout. JSON preserves technical identifiers and supplied data. Invalid input exits with code 2.

## Español

Comparar tolerancias extremas e hipótesis estadísticas.

Datos sintéticos; no requiere red ni secretos.

```sh
python -m tolerance_stack_corners examples/demo.json --lang es
python -m unittest discover -s tests -v
```

### Método y diferencia

Comparar tolerancias extremas e hipótesis estadísticas: cálculo determinista con entradas estructuradas, testigos y casos límite explícitos.

### Límites

Modelo acotado y datos ficticios; ningún servicio ni hardware de producción validado. Métodos clásicos; sin superioridad SOTA general ni adopción humana demostrada.

### Validación

Pruebas de dominio, casos límite e interfaz FR/EN/ES. CI prueba Python 3.11/3.13 y ejecuta la wheel instalada fuera del repositorio. JSON conserva identificadores técnicos y datos proporcionados. Entrada inválida termina con código 2.

## Sources / Fuentes

- https://www.itl.nist.gov/div898/handbook/pmc/section3/pmc323.htm

## Projets voisins / Neighboring projects / Proyectos vecinos

FR : [gauge-rr-crossed](https://github.com/gbesse/gauge-rr-crossed) est un autre diagnostic du portefeuille. Ici : Comparer tolérances extrêmes et hypothèses statistiques. Comparaison de périmètres seulement, sans affiliation ni benchmark de supériorité.

EN: [gauge-rr-crossed](https://github.com/gbesse/gauge-rr-crossed) is a different portfolio diagnostic. Here: Compare worst-case tolerances and statistical assumptions. Scope comparison only, no affiliation or superiority benchmark.

ES: [gauge-rr-crossed](https://github.com/gbesse/gauge-rr-crossed) es otro diagnóstico del portafolio. Aquí: Comparar tolerancias extremas e hipótesis estadísticas. Comparación de alcance, sin afiliación ni benchmark de superioridad.

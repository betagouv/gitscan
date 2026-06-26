## Changelog : plusfraisautravail (30 derniers jours, au 25 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'intégration d'un nouveau moteur de calcul de score basé sur Publicodes pour l'auto-diagnostic, ainsi que sur l'amélioration significative du widget d'alerte canicule. Ce dernier bénéficie d'une nouvelle approche pour l'affichage de la carte, avec un chargement à la demande et une meilleure isolation, offrant une expérience utilisateur plus fluide et performante.

### Évolutions fonctionnelles
- **Auto-diagnostic :** Migration du moteur de calcul de score vers les règles Publicodes, permettant une plus grande flexibilité et maintenabilité. [#5fe8f7c](https://github.com/incubateur-ademe/plusfraisautravail/commit/5fe8f7c)
- **Widget d'alerte canicule :**
    - Ajout d'une route `/map` affichant la carte de vigilance canicule de la France et des DROM-TOM. [#a03bf75](https://github.com/incubateur-ademe/plusfraisautravail/commit/a03bf75)
    - Amélioration du chargement de la carte : le bundle de la carte est maintenant chargé à la demande avec isolation via Shadow DOM. [#02f52e8](https://github.com/incubateur-ademe/plusfraisautravail/commit/02f52e8)
    - Suppression de l'affichage de la barre d'adresse du navigateur sur la route `/map` et configuration du proxy de développement pour pointer vers l'API de production. [#910b556](https://github.com/incubateur-ademe/plusfraisautravail/commit/910b556)
    - La carte est maintenant intégrée directement à la position du script, supprimant l'affichage d'un flash de chargement. [#4f3dd25](https://github.com/incubateur-ademe/plusfraisautravail/commit/4f3dd25)
    - Correction : le lien de prévention s'ouvre maintenant dans le même onglet. [#d4eb811](https://github.com/incubateur-ademe/plusfraisautravail/commit/d4eb811)
- **Carte canicule :** Affichage filtré uniquement des canicules sur la carte. [#e7ed19e](https://github.com/incubateur-ademe/plusfraisautravail/commit/e7ed19e)

### Évolutions techniques
- Intégration de Publicodes pour le moteur de scoring de l'auto-diagnostic. [#5fe8f7c](https://github.com/incubateur-ademe/plusfraisautravail/commit/5fe8f7c)
- Refonte de l'intégration de la carte du widget d'alerte pour améliorer les performances et l'isolation. [#02f52e8](https://github.com/incubateur-ademe/plusfraisautravail/commit/02f52e8)

### Autres changements
- Mise à jour du contenu de l'application. [#1dbc140](https://github.com/incubateur-ademe/plusfraisautravail/commit/1dbc140)

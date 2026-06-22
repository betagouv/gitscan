## Changelog : OTP-DS-to-Grist (30 derniers jours, au 2026-06-19)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion des configurations et l'ajout de la prise en charge de plusieurs volets dans Grist. Des corrections ont également été apportées pour améliorer la stabilité et l'expérience utilisateur, notamment concernant le tutoriel et la gestion des tables répétables. Enfin, de nombreuses dépendances ont été mises à jour pour assurer la sécurité et la performance de l'application.

### Évolutions fonctionnelles
- **Gestion des configurations :** L'API permet désormais de gérer plusieurs configurations. [#309](https://github.com/betagouv/OTP-DS-to-Grist/issues/309)
- **Prise en charge de plusieurs volets Grist :** Possibilité de synchroniser les données vers plusieurs volets dans Grist. [#358](https://github.com/betagouv/OTP-DS-to-Grist/issues/358)
- **Amélioration du tutoriel :** Correction de problèmes liés au tutoriel. [#346](https://github.com/betagouv/OTP-DS-to-Grist/issues/346)
- **Correction de la création de tables répétables :** Suppression de la création inutile de la table générique `_repetable_rows`. [#347](https://github.com/betagouv/OTP-DS-to-Grist/issues/347)
- **Correction du chemin du manifest Vue :** Correction d'un problème de chemin pour le manifest Vue.
- **Mise à jour de l'interface Vue :** Plusieurs petites améliorations de l'interface Vue. [#340](https://github.com/betagouv/OTP-DS-to-Grist/issues/340)

### Évolutions techniques
- **Installation de Vue.js :** Ajout de l'installation de Vue.js pour le frontend. [#328](https://github.com/betagouv/OTP-DS-to-Grist/issues/328) et [#342](https://github.com/betagouv/OTP-DS-to-Grist/issues/342)
- **Normalisation des noms de colonnes :** Amélioration de la fonction de normalisation des noms de colonnes pour gérer correctement les longueurs maximales. [#355](https://github.com/betagouv/OTP-DS-to-Grist/issues/355)

### Autres changements
- **Mise à jour des dépendances :** De nombreuses dépendances ont été mises à jour vers leurs dernières versions (urllib3, form-data, ruff, pytest, cryptography, baseline-browser-mapping, eslint, python-socketio, sqlalchemy, psycopg2-binary, requests, commitizen, jest, eventlet).

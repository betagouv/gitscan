## Changelog : OTP-DS-to-Grist (30 derniers jours, au 25 juin 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la gestion des configurations, notamment la possibilité de gérer plusieurs configurations simultanément, de les charger et de les sauvegarder. Des corrections de bugs ont également été apportées pour améliorer la stabilité et l'expérience utilisateur. Enfin, des mises à jour de dépendances ont été effectuées pour maintenir la sécurité et la performance du projet.

### Évolutions fonctionnelles
- **Gestion des configurations :** Possibilité de supprimer plusieurs configurations à la fois. [#373](https://github.com/betagouv/OTP-DS-to-Grist/issues/373)
- **Gestion des configurations :** Implémentation du chargement d'une configuration existante. [#372](https://github.com/betagouv/OTP-DS-to-Grist/issues/372)
- **Gestion des configurations :** Possibilité de sauvegarder une configuration individuelle. [#371](https://github.com/betagouv/OTP-DS-to-Grist/issues/371)
- **Interface utilisateur :** Ajout d'un volet dédié à la gestion des données dans Démarches Simplifiées (DN). [#362](https://github.com/betagouv/OTP-DS-to-Grist/issues/362)
- **Interface utilisateur :** Ajout d'un volet dédié à Grist pour la configuration. [#358](https://github.com/betagouv/OTP-DS-to-Grist/issues/358)
- **Tutoriel :** Modification du tutoriel pour plus de clarté. [#346](https://github.com/betagouv/OTP-DS-to-Grist/issues/346)
- **API :** L'API gère désormais plusieurs configurations. [#309](https://github.com/betagouv/OTP-DS-to-Grist/issues/309)
- **Vue JS :** Installation de Vue.js pour l'interface utilisateur. [#328](https://github.com/betagouv/OTP-DS-to-Grist/issues/328)
- **Vue JS :** Installation de DSFR (Design System FR) pour Vue.js. [#342](https://github.com/betagouv/OTP-DS-to-Grist/issues/342)

### Évolutions techniques
- **Normalisation des noms de colonnes :** Correction du paramètre `max_length` dans la fonction `normalize_column_name` pour éviter des erreurs. [#355](https://github.com/betagouv/OTP-DS-to-Grist/issues/355)
- **Base de données :** Suppression de la création de la table générique `_repetable_rows` qui n'était plus nécessaire. [#347](https://github.com/betagouv/OTP-DS-to-Grist/issues/347)
- **Correction d'un bug :** Correction d'un message d'erreur persistant. [#315](https://github.com/betagouv/OTP-DS-to-Grist/issues/315)
- **Hotfix Vue JS:** Correction du chemin du manifest et mise à jour de la vue. [#340](https://github.com/betagouv/OTP-DS-to-Grist/issues/340)

### Autres changements
- Documentation mise à jour.
- Nettoyage du code.
- Mises à jour de dépendances (urllib3, form-data, ruff, pytest, cryptography, baseline-browser-mapping, eslint, python-socketio, sqlalchemy, eventlet, commitizen, jest, jest-environment-jsdom).

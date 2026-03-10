## Changelog : diagbruit.beta.gouv.fr (30 derniers jours)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de la gestion des zones bruyantes, l'ajout de pages légales, et la refactorisation de l'interface utilisateur pour une meilleure expérience. Des corrections ont également été apportées pour gérer correctement les polygones de sources de bruit et améliorer la stabilité de l'application.

### Évolutions fonctionnelles
- Ajout d'une alerte spécifique si une zone bruyante est atteinte [#40](https://github.com/betagouv/diagbruit.beta.gouv.fr/pulls/40).
- Affichage de la recommandation calculée directement sur la page du permis de construire (PEB) [#45](https://github.com/betagouv/diagbruit.beta.gouv.fr/pulls/45) et [#48](https://github.com/betagouv/diagbruit.beta.gouv.fr/pulls/48).
- Ajout de toutes les pages légales nécessaires au site [#44](https://github.com/betagouv/diagbruit.beta.gouv.fr/pulls/44).
- Amélioration de l'affichage du résumé, avec une refactorisation des composants et du texte [#42](https://github.com/betagouv/diagbruit.beta.gouv.fr/pulls/42).
- Ajout d'un iframe pour l'intégration de Tally [#42](https://github.com/betagouv/diagbruit.beta.gouv.fr/pulls/42).
- Gestion des sources de bruit avec des polygones [#41](https://github.com/betagouv/diagbruit.beta.gouv.fr/pulls/41).

### Évolutions techniques
- Refactorisation du code frontend pour améliorer la structure et la maintenabilité.
- Adaptation des scripts d'ingestion pour tenir compte des changements en production.
- Mise en place d'une configuration pour l'utilisation de Corepack Yarn.
- Amélioration de la configuration du CMS pour réduire la taille de l'image Docker et optimiser le déploiement.
- Ajout de la gestion des zones bruyantes dans la base de données et l'API FastAPI [#40](https://github.com/betagouv/diagbruit.beta.gouv.fr/pulls/40).
- Correction de bugs et amélioration de la robustesse des tests.

### Autres changements
- Ajout de fichiers de configuration CLAUDE.md [#47](https://github.com/betagouv/diagbruit.beta.gouv.fr/pulls/47).
- Mise à jour des labels et descriptions des zones bruyantes dans l'API [#43](https://github.com/betagouv/diagbruit.beta.gouv.fr/pulls/43).
- Ouverture de la whitelist pour les codes 35, 59 et 67 [#39](https://github.com/betagouv/diagbruit.beta.gouv.fr/pulls/39).
- Suppression des références aux PLU locaux en attendant une implémentation future.
- Corrections mineures de design et d'UX sur l'interface utilisateur.
- Suppression de messages de défense sur la page PEB.
- Suppression du badge "work in progress".
- Bump de la version de l'API.

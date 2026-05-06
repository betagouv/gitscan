## Changelog : signalconso-website (30 derniers jours, au 01 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la gestion des signalements et l'expérience utilisateur. Des corrections ont été apportées au sélecteur de pays et à l'affichage des catégories de signalement. De plus, des ajustements ont été effectués concernant la gestion des fichiers et la génération des actualités.

### Évolutions fonctionnelles
- Correction du sélecteur de pays dans le formulaire de signalement [#1123](https://github.com/betagouv/signalconso-website/pull/1123).
- Suppression de l'ancienne version (v1) de l'endpoint des catégories de signalement [#1121](https://github.com/betagouv/signalconso-website/pull/1121).
- Possibilité de sélectionner une entreprise étrangère dans le parcours de signalement Bat [#1117](https://github.com/betagouv/signalconso-website/pull/1117).
- Mise à jour du libellé des catégories de signalement [#1118](https://github.com/betagouv/signalconso-website/pull/1118).

### Évolutions techniques
- Sanityzation manuelle des noms de fichiers des anomalies pour améliorer la sécurité et la robustesse du système [#1117](https://github.com/betagouv/signalconso-website/pull/1117).
- Désactivation de la génération du flux d'actualités, car il n'est plus utilisé sans l'application mobile.

### Autres changements
- Nettoyage et amélioration de la gestion des noms de fichiers des anomalies.

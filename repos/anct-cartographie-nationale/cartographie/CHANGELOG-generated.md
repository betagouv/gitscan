## Changelog : cartographie (30 derniers jours, au 10 juillet 2026)

### Résumé
Cette version apporte des améliorations de la stabilité et de l'observabilité de l'application, notamment au niveau de la gestion du cache et des erreurs. Une nouvelle fonctionnalité de filtrage par source de données a été ajoutée, offrant aux utilisateurs plus de contrôle sur les données affichées.

### Évolutions fonctionnelles
- Ajout d'un filtre par source de données pour affiner les résultats de recherche. [#a4f4fd0](https://github.com/anct-cartographie-nationale/cartographie/commit/a4f4fd0662c3b76ef8563c42dfb092e52e307a16)
- Amélioration de la gestion des erreurs lors de la soumission du formulaire de contact : les messages d'erreur du serveur sont maintenant traduits pour une meilleure compréhension par l'utilisateur. [#94c0c6b](https://github.com/anct-cartographie-nationale/cartographie/commit/94c0c6b13b0c9618de7ce7822b3d16c9219737b0)
- Correction d'un problème d'affichage des toasts (notifications) au-dessus de la fenêtre modale de contact. [#d3dbb1d](https://github.com/anct-cartographie-nationale/cartographie/commit/d3dbb1d1d3a1a2aaf85c2a97c0b8e006d307b3ea)

### Évolutions techniques
- Refactorisation du cache des lieux pour une meilleure gestion et un partage efficace entre les différentes parties de l'application. [#c3c854a](https://github.com/anct-cartographie-nationale/cartographie/commit/c3c854a) et [#5053aac](https://github.com/anct-cartographie-nationale/cartographie/commit/5053aac)
- Instrumentation du cache des lieux pour faciliter le diagnostic des problèmes de données obsolètes. [#052847a](https://github.com/anct-cartographie-nationale/cartographie/commit/052847a)
- Mise à jour des dépendances et adaptation de la configuration Biome pour la version 2.5. [#83d4e24](https://github.com/anct-cartographie-nationale/cartographie/commit/83d4e24) et [#1f3b970](https://github.com/anct-cartographie-nationale/cartographie/commit/1f3b970)
- Amélioration de l'observabilité avec l'ajout de logs structurés et la corrélation avec Sentry via un identifiant de requête.
- Ajout de logs d'accès Nginx au format JSON pour faciliter l'analyse avec Grafana.
- Capture des échecs de préchargement du cache au démarrage de l'application.

### Autres changements
- Utilisation de la notation par points pour accéder aux variables d'environnement. [#f7deebe](https://github.com/anct-cartographie-nationale/cartographie/commit/f7deebe)
- Mise à jour des actions GitHub (actions/checkout et actions/cache) vers leurs dernières versions. [#87ee084](https://github.com/anct-cartographie-nationale/cartographie/commit/87ee084)
- Migration des imports de `react-email` vers un package unifié. [#7154acb](https://github.com/anct-cartographie-nationale/cartographie/commit/7154acb)

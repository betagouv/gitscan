## Changelog : cartographie (30 derniers jours, au 26 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'observabilité, la robustesse et la modernisation de l'infrastructure. De nouvelles fonctionnalités de filtrage ont été ajoutées, et l'application est désormais mieux instrumentée pour le suivi des erreurs et des performances, facilitant ainsi la maintenance et l'amélioration continue. Des refactorings importants ont également été effectués pour adopter des bibliothèques plus modernes et standardisées.

### Évolutions fonctionnelles
- Ajout d'un filtre par source de données pour affiner les recherches et l'affichage des lieux d'inclusion numérique. [#a4f4fd0](https://github.com/anct-cartographie-nationale/cartographie/commit/a4f4fd0662c3b76ef8563c42dfb092e52e307a16)

### Évolutions techniques
- **Observabilité :** Corrélation des logs Nginx et Sentry via un `request_id` pour faciliter le débogage et le suivi des requêtes. [#aba6a86](https://github.com/anct-cartographie-nationale/cartographie/commit/aba6a868f0209a98c268ec1bab160acaa70f64cb)
- **Observabilité :** Émission des logs d'accès Nginx au format JSON pour une meilleure intégration avec Grafana. [#4614093](https://github.com/anct-cartographie-nationale/cartographie/commit/4614093beeec01fdca6e79da0d859f4b5bc7cf1d)
- **Cache :** Amélioration de la gestion du cache pour éviter les erreurs et assurer une meilleure cohérence des données.  Attente de la fin du rafraîchissement de la mémoire avant d'invalider le cache Next.js. [#2ea5904](https://github.com/anct-cartographie-nationale/cartographie/commit/2ea59047881c3fd73c55f3920b246f01c0410482)
- **Infrastructure :** Réduction du TTL du cache Nginx à 5 minutes pour une propagation plus rapide des mises à jour. [#62b786b](https://github.com/anct-cartographie-nationale/cartographie/commit/62b786b964660d14a808ca038cd8870e92d2883c)
- **Télémetrie :** Intégration de Sentry pour la remontée des erreurs, avec filtrage des informations personnelles et des logs inutiles. [#5f631b9](https://github.com/anct-cartographie-nationale/cartographie/commit/5f631b9549b48474f0146679426f30a8197f9d47)
- **Télémetrie :** Capture des erreurs dans les routes d'export CSV, l'action de contact et la récupération des données de la carte. [#d2e357b](https://github.com/anct-cartographie-nationale/cartographie/commit/d2e357b4791c1046a3a1673b9438692474043401)
- **Refactoring :** Adoption de `@arckit/nextjs` et suppression des utilitaires locaux absorbés, simplifiant ainsi la configuration et la maintenance de Next.js. [#7af3a5d](https://github.com/anct-cartographie-nationale/cartographie/commit/7af3a5d4a8f34266455720954343431591431f19)
- **Refactoring :** Migration vers `@arckit/form` pour une gestion plus standardisée des formulaires. [#52943dc](https://github.com/anct-cartographie-nationale/cartographie/commit/52943dc4576f453243954a1b6372827472977b67)
- **Refactoring :** Adoption de `@arckit/daisyui` pour les composants d'interface utilisateur standardisés. [#efb60f8](https://github.com/anct-cartographie-nationale/cartographie/commit/efb60f81390f805106416770386a347609576568)
- **CI/CD :** Mise à jour des dépendances et configuration de l'environnement CI pour supporter Sentry auto-hébergé. [#d45720b](https://github.com/anct-cartographie-nationale/cartographie/commit/d45720b491264a9439794434996814940f68443b)

### Autres changements
- Documentation de la configuration de l'observabilité et de la capture d'erreurs. [#385ae69](https://github.com/anct-cartographie-nationale/cartographie/commit/385ae69152486f45f29266163b41936463706991)
- Documentation de la capture de démarrage du cache pour l'observabilité. [#c82b42c](https://github.com/anct-cartographie-nationale/cartographie/commit/c82b42c3b637840815a04274c07699434639478c)
- Documentation de la journalisation structurée du serveur. [#77f33e2](https://github.com/anct-cartographie-nationale/cartographie/commit/77f33e20443688129f6519667665568099662197)
- Mise à jour des dépendances `@arckit/nextjs` et `@arckit/resultset` vers la version 2.0.0. [#9f4f664](https://github.com/anct-cartographie-nationale/cartographie/commit/9f4f664939893714492455878139897f8111816a)
- Epinglage de la version de Node.js à 24 dans le CI. [#519e14d](https://github.com/anct-cartographie-nationale/cartographie/commit/519e14d969942198629b42790974f870642374f5)

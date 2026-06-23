## Changelog : cartographie (30 derniers jours, au 16 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'observabilité et la robustesse de l'application. Des outils de surveillance et de journalisation plus performants ont été intégrés pour faciliter le diagnostic et la résolution des problèmes.  De plus, un formulaire de contact a été ajouté pour permettre aux utilisateurs de contacter l'équipe de développement.

### Évolutions fonctionnelles
- Ajout d'un formulaire de contact avec envoi d'emails via SMTP. [#3940337](https://github.com/anct-cartographie-nationale/cartographie/commit/3940337f61459f11a339797a5614925890f6484d)
- Amélioration de l'expérience utilisateur du formulaire de contact avec un texte d'introduction mis à jour et des liens vers la documentation et une vidéo explicative. [#546ff4a](https://github.com/anct-cartographie-nationale/cartographie/commit/546ff4a909654976273c8453669135241f040842)
- Ajout d'un indicateur de temps de dernier rafraîchissement du cache à l'endpoint de santé. [#f9a4d09](https://github.com/anct-cartographie-nationale/cartographie/commit/f9a4d091cfd0104b3f52890c99c7c2626cf3efc0)

### Évolutions techniques
- Mise en place d'une journalisation structurée des requêtes serveur pour faciliter le débogage et l'analyse. [#73141cd](https://github.com/anct-cartographie-nationale/cartographie/commit/73141cd04f8d391968f2379b05f1f24281ba5d75)
- Intégration de Sentry pour la capture et le suivi des erreurs applicatives. [#4f1548d](https://github.com/anct-cartographie-nationale/cartographie/commit/4f1548da416f412906d5972682f3bf2088b7c699)
- Amélioration de la corrélation entre les logs Nginx et les événements Sentry grâce à l'ajout d'un `request_id`. [#aba6a86](https://github.com/anct-cartographie-nationale/cartographie/commit/aba6a868f0209a98c268ec1bab160acaa70f64cb)
- Configuration de Nginx pour émettre des logs d'accès au format JSON, facilitant leur analyse avec Grafana. [#4614093](https://github.com/anct-cartographie-nationale/cartographie/commit/4614093beeec01fdca6e79da0d859f4b5bc7cf1d)
- Refactorisation importante de l'architecture Next.js avec l'adoption de `@arckit/nextjs` et suppression d'utilitaires locaux. [#75eedea](https://github.com/anct-cartographie-nationale/cartographie/commit/75eedea4606524a7991f397a88f3756761886699)
- Refactorisation de la gestion des formulaires avec l'adoption de `@arckit/form`. [#52943dc](https://github.com/anct-cartographie-nationale/cartographie/commit/52943dc4994629623c684644d591159351574478)
- Adoption de `@arckit/daisyui` pour les composants d'interface utilisateur standard. [#efb60f8](https://github.com/anct-cartographie-nationale/cartographie/commit/efb60f857429549969665039415062491472297a)
- Mise à jour de plusieurs dépendances, notamment `@arckit/nextjs`, `@arckit/resultset` et `@arckit/form`. [#58fe28c](https://github.com/anct-cartographie-nationale/cartographie/commit/58fe28c1942645906913f295289010497441732d)
- Amélioration de la gestion des erreurs et des retries pour le chargement des données en cache. [#fe3379e](https://github.com/anct-cartographie-nationale/cartographie/commit/fe3379e7411d926df311a99dc26a3f4eb1d1ffff)

### Autres changements
- Ajout de tests pour l'endpoint de santé avec prise en compte du nouveau champ `cache`. [#fa61024](https://github.com/anct-cartographie-nationale/cartographie/commit/fa61024996453781a5b16749364340996066399a)
- Documentation de la capture du warm-up du cache au démarrage. [#c82b42c](https://github.com/anct-cartographie-nationale/cartographie/commit/c82b42c444560b7693947c5a94a60b74b7f3a563)
- Ajout d'une documentation sur l'observabilité et la capture d'erreurs. [#385ae69](https://github.com/anct-cartographie-nationale/cartographie/commit/385ae69646998183f2a99c6984809819595f996a)
- Configuration de gitleaks pour la détection de secrets dans le code et les commits. [#f24c364](https://github.com/anct-cartographie-nationale/cartographie/commit/f24c36452713134f567296502f451b9000f2b841)

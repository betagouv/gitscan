## Changelog : mobilic (30 derniers jours, au 18/08/2026)

### Résumé
Les récentes évolutions se concentrent sur l'amélioration de la cohérence des données et de l'expérience utilisateur. L'historique des activités dans l'application est désormais parfaitement aligné avec les documents PDF exportés. Nous avons également fluidifié la saisie des informations (notamment les dates de naissance) et affiné la gestion des statuts de mission pour les administrateurs et les employés.

### Évolutions fonctionnelles
- **Saisie et formulaires** : Amélioration de l'expérience de saisie de la date de naissance avec un système de focus automatique optimisé et une validation plus robuste [#924](https://github.com/MTES-MCT/mobilic/pull/924). Suppression de la fenêtre d'alerte concernant les missions longues pour les employés afin de simplifier leur parcours [#908](https://github.com/MTES-MCT/mobilic/pull/908).
- **Historique et notifications** : Harmonisation de l'historique des activités dans l'application (PWA) avec les exports PDF (textes, motifs, types de contestation) pour éviter toute confusion [#910](https://github.com/MTES-MCT/mobilic/pull/910). Ajout d'un tag "MODIFICATION" pour identifier clairement les activités scindées au lieu du tag "AJOUT" [#912](https://github.com/MTES-MCT/mobilic/pull/912). Optimisation de l'affichage des notifications sur les écrans mobiles [#906](https://github.com/MTES-MCT/mobilic/pull/906).
- **Gestion administrative** : Optimisation de la gestion des statuts de mission, notamment pour assurer la continuité du statut "en cours" jusqu'à la fin de la mission par l'employé [#913](https://github.com/MTES-MCT/mobilic/pull/913). Amélioration de la traçabilité et de la création de missions lors des sessions d'impersonnalisation [#910](https://github.com/MTES-MCT/mobilic/pull/910). Renforcement des détails dans les bannières de contestation pour les administrateurs.

### Évolutions techniques
- **Infrastructure et CI/CD** : Amélioration de la stabilité et de la configuration des environnements de test (Review Apps via Scalingo) [#904](https://github.com/MTES-MCT/mobilic/pull/904), [#921](https://github.com/MTES-MCT/mobilic/pull/921). Optimisation des scripts de détection de branche dans le pipeline de CI.
- **Refactoring** : Centralisation de la logique de calcul des statuts de mission pour garantir une cohérence totale entre les différentes vues administratives. Simplification de plusieurs composants UI (notamment la gestion de l'affichage des durées) pour réduire la complexité du code.

## Changelog : proconnect-espace-partenaires (30 derniers jours, au 18 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la documentation, la correction de problèmes d'intégration avec la fédération et la préparation de l'application pour la maintenance. Des ajustements ont également été apportés à la configuration des tests E2E et à la gestion des bases de données.

### Évolutions fonctionnelles
- Ajout d'un mode maintenance pour désactiver les modifications de l'espace partenaire. [#312](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/312)
- Amélioration de la documentation concernant la configuration de l'authentification multifactorielle (MFA) avec LemonLDAP::NG. [#316](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/316)
- Clarification dans la documentation que les informations sur l'utilisateur (claims) sont renvoyées via l'endpoint `/user-info`. [#322](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/322)
- Ajout d'une mention de l'organisation et du SIRET professionnel. [#330](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/330)
- Ajout de précision concernant l'Eidas1 lorsque les ACrs ne sont pas gérés. [#323](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/323)
- Ajout de documentation sur les scopes des rôles. [#331](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/331)

### Évolutions techniques
- Renommage de la base de données MongoDB en "corev2" et de l'utilisateur en "proconnect-app-api-partner". [#337](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/337)
- Correction de la configuration du serveur web UUV dans les tests E2E et résolution d'un problème d'assertion de chargement intermittent.
- Rétractation d'une mise à jour de la librairie `nodemailer`. [#335](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/335)
- Mises à jour de dépendances : `axios`, `fast-xml-builder`, `fast-uri`, `postcss`, `typescript`, `next`.
- Mise à jour de la dépendance `proconnect-gouv/federation/api-partner`. [#327](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/327), [#334](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/334), [#315](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/315)
- Mise à jour de la librairie `@uuv/playwright`. [#333](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/333)

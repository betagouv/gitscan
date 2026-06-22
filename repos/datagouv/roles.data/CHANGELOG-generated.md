## Changelog : roles.data (30 derniers jours, au 19 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'amélioration de la robustesse et du débogage de l'application, notamment en anonymisant les informations sensibles dans les logs d'erreur et en ajoutant des détails aux logs d'exceptions. Des corrections ont également été apportées pour normaliser les adresses email lors de l'ajout d'utilisateurs à des groupes par un administrateur et pour mettre à jour les valeurs ACR.

### Évolutions fonctionnelles
- Correction : Normalisation des adresses email avant l'ajout d'utilisateurs à un groupe par un administrateur. Cela assure une gestion plus cohérente des utilisateurs et évite les doublons potentiels.  [#160](https://github.com/datagouv/roles.data/issues/160)
- Mise à jour : Les valeurs ACR (Attribute Certificate Request) ont été mises à jour. [#163](https://github.com/datagouv/roles.data/issues/163)

### Évolutions techniques
- Amélioration : Anonymisation des adresses email dans les exceptions envoyées à Sentry. Cela permet de protéger la vie privée des utilisateurs tout en conservant des informations utiles pour le débogage. [#162](https://github.com/datagouv/roles.data/issues/162)
- Amélioration : Ajout de détails sur les erreurs dans les logs pour les exceptions `HttpException`. Cela facilite l'identification et la résolution des problèmes liés aux requêtes HTTP. [#161](https://github.com/datagouv/roles.data/issues/161)

### Autres changements
- Diverses petites modifications et corrections (commits "www:minor" et "dev:minor") pour améliorer la maintenance et la qualité du code.

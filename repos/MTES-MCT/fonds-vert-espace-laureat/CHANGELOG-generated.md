## Changelog : fonds-vert-espace-laureat (30 derniers jours)

### Résumé
Cette mise à jour apporte des corrections pour améliorer la robustesse de l'application, notamment lors de la gestion des données provenant de l'API Grist. Des mises à jour de dépendances ont également été effectuées pour maintenir la sécurité et la stabilité du projet.

### Évolutions fonctionnelles
- Correction d'un bug qui se produisait lorsque le champ "action" de l'API Grist était nul. L'application gère maintenant correctement ces cas, évitant ainsi des erreurs lors du pré-remplissage des données. [#247aa3b](https://github.com/MTES-MCT/fonds-vert-espace-laureat/commit/247aa3b)

### Évolutions techniques
- Mise à jour des dépendances du projet, incluant `@graphql-codegen/cli` et `client-preset` vers les versions 6 et 5 respectivement. [#2a342df](https://github.com/MTES-MCT/fonds-vert-espace-laureat/commit/2a342df)
- Mise à jour de plusieurs packages pour assurer la compatibilité et la sécurité. [#ed4a59f](https://github.com/MTES-MCT/fonds-vert-espace-laureat/commit/ed4a59f)
- Correction de problèmes liés à l'immutabilité et à la configuration de `postcss-url`. [#7734773](https://github.com/MTES-MCT/fonds-vert-espace-laureat/commit/7734773), [#4dec6c3](https://github.com/MTES-MCT/fonds-vert-espace-laureat/commit/4dec6c3)

### Autres changements
- Ajout de logs pour les enregistrements Grist avec un champ "action" invalide, facilitant le débogage et l'identification des problèmes de données. [#24941b1](https://github.com/MTES-MCT/fonds-vert-espace-laureat/commit/24941b1)

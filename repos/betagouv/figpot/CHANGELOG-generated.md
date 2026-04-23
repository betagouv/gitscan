## Changelog : figpot (30 derniers jours, au 22 avril 2026)

### Résumé
Cette version apporte des améliorations significatives à la synchronisation Figma vers Penpot, notamment concernant la gestion des grilles, des booléens et des flottants. Des corrections ont été apportées pour gérer les nouvelles limitations de l'API Figma et les changements d'API Penpot. Des améliorations de la robustesse et de la gestion des erreurs ont également été intégrées.

### Évolutions fonctionnelles
- Amélioration de la synchronisation des grilles : les métadonnées des cellules de grille sont maintenant correctement transférées, évitant ainsi la rupture de la structure de la grille dans Penpot.
- Gestion améliorée des booléens : les nœuds booléens de Penpot acceptent maintenant le format SVG pour la propriété `content`, assurant une meilleure compatibilité.
- Précision accrue des flottants : la tolérance de comparaison des flottants a été ajustée pour une meilleure correspondance entre Figma et Penpot.
- Possibilité de forcer des spécificités de police : une nouvelle fonctionnalité permet de forcer des spécificités de police lors de la synchronisation via un motif de remplacement. [#1234](https://github.com/betagouv/figpot/issues/1234)
- Information sur les limitations de l'API Figma : un message informatif a été ajouté concernant la nouvelle politique de limitation de débit de l'API Figma et propose des solutions possibles.
- Utilisation du cache Figma : l'utilisation du cache Figma est maintenant privilégiée pour éviter les requêtes inutiles à l'API Figma.

### Évolutions techniques
- Mise à jour des endpoints Penpot : le code a été mis à jour pour utiliser les nouveaux chemins d'accès aux endpoints de l'API Penpot.
- Correction de problèmes liés à l'exécution avec `npx` : une tentative de résolution d'un problème rencontré lors de l'exécution de `figpot` avec `npx` a été implémentée.
- Correction de formatage du `package.json` : le fichier `package.json` a été corrigé pour éviter les avertissements npm.
- Correction de l'échappement des backslashes sous Windows : les backslashes dans les chemins d'accès sont maintenant correctement gérés sous Windows.

### Autres changements
- Nettoyage du fichier `lockfile`.
- Ajout d'une mention concernant les avertissements de Playwright lors de l'installation.
- Mise à jour de la version Node pour éviter un avertissement npm.
- Correction de la gestion de la suppression des miniatures.
- Correction de la gestion des erreurs lors de la récupération des variables locales Figma avec un plan incorrect.

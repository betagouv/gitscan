## Changelog : ami-design-system-ios (30 derniers jours, au 13 mai 2026)

### Résumé
Cette version apporte des améliorations significatives à la structure du projet et à l'exposition de ses composants. De nouveaux composants, comme la vue "TileView" et les "Pills", ont été ajoutés, et des ajustements ont été faits pour faciliter l'intégration du système de design dans d'autres projets.

### Évolutions fonctionnelles
- Ajout d'un nouveau composant "TileView" permettant d'afficher des informations structurées avec un titre et un texte multilignes alignés à gauche.
- Migration des types de vues "Pills" dans le package, offrant une nouvelle option de style pour les éléments d'interface.

### Évolutions techniques
- Refactorisation de la structure du projet : les fichiers Swift et les ressources du système de design ont été déplacés dans un sous-dossier "DesignSystem".
- Les composants sont maintenant publics, facilitant leur utilisation et leur extension par les développeurs.
- La propriété `body` des composants est désormais publique pour respecter le protocole `View`.
- Modification de la structure du package pour que le fichier `Package.swift` se trouve à la racine du dépôt GitHub, simplifiant l'intégration dans d'autres projets.
- Correction de la description du build.
- Suppression des fichiers de ressources inutilisés.

### Autres changements
- Mise à jour du script de génération de projet d'exemple et du fichier README.
- Ajout d'un initialisateur public pour les composants.
- Correction de problèmes identifiés par le linter.

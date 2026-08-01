## Changelog : ui-kit (30 derniers jours, au 31 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à la gestion des fichiers et des contacts, notamment avec l'ajout de composants pour le téléchargement et l'importation de fichiers, ainsi que des améliorations de l'accessibilité et de l'expérience utilisateur. Des corrections de bugs et des optimisations ont également été apportées.

### Évolutions fonctionnelles
- Ajout d'un composant de téléchargement de fichiers avec gestion des états de la zone de dépôt et des retours d'information à l'utilisateur.
- Implémentation d'un modal d'importation de contacts via un fichier.
- Amélioration de l'accessibilité du composant `StorageGauge` (indicateur de stockage).
- Ajout d'un composant d'alerte personnalisable avec des icônes.
- Ajout d'une option de réinitialisation dans les filtres et champs de recherche.
- Amélioration de la gestion des menus utilisateurs, notamment sur mobile.
- Centrage des boutons dans les modales sur mobile.
- Ajout d'un composant `UserAvatar` avec dégradé linéaire.

### Évolutions techniques
- Refactorisation du composant de téléchargement de fichiers pour une meilleure organisation du code.
- Mise à jour de la librairie `cunningham-react` vers la version 4.4.0.
- Suppression de code inutilisé lié au téléchargement de fichiers.
- Amélioration de la structure des tests E2E pour les modales et les indicateurs de stockage.
- Utilisation de composants `Icon` pour les affordances des éléments de menu.
- Extraction de composants réutilisables pour améliorer la cohérence et la maintenabilité.

### Autres changements
- Documentation des changements de branche dans le fichier `CHANGELOG.md`.
- Correction de liens vers la documentation de Cunningham dans les stories.
- Amélioration de la lisibilité du code avec l'ajout de nouvelles lignes.
- Correction de l'assertion d'une ligne d'entrée dans les tests du champ de recherche.
- Traduction des textes liés au téléchargement et à l'importation de fichiers.
- Ajout d'une catégorie de documentation "mime" pour les documents.
- Mise à jour des icônes.

## Changelog : gestion-des-subventions-locales (30 derniers jours, au 11 septembre 2026)

### Résumé
Cette période est marquée par une amélioration majeure des processus de notification et de gestion documentaire. L'outil permet désormais de générer massivement des lettres de refus, de télécharger l'ensemble des documents en un clic et d'automatiser le suivi des documents signés via QR code. L'interface a également été modernisée pour être plus fluide et accessible.

### Évolutions fonctionnelles
- **Notifications et gestion des refus** : Mise en place de la génération en masse des lettres de refus ou de classement sans suite [#833], intégration du scan de QR codes pour rattacher automatiquement les lettres signées [#850] et amélioration de l'affichage des informations de notification [#857].
- **Gestion documentaire** : Ajout d'un bouton pour télécharger tous les documents générés simultanément [#802], possibilité d'uploader des documents pour les lettres de refus [#832] et introduction d'un onglet de suivi financier (en phase de test) [#815].
- **Expérience utilisateur (UX) et Accessibilité** : Fluidification des formulaires (zonage, budget vert, avis de commission) grâce à l'utilisation de HTMX [#812, #809, #807], ajout de retours visuels (loaders) lors de la sauvegarde et renforcement de l'accessibilité (gestion des icônes et emojis) [#778].
- **Corrections** : Résolution de problèmes d'affichage des menus déroulants en bas de page [#884] et correction de bugs sur les actions de "retour en construction" [#874].

### Évolutions techniques
- **Architecture et Refactoring** : Réorganisation profonde de la structure du projet (déplacement de modules vers des sous-packages dédiés comme `gsl.projet`, `gsl.simulation`, `gsl.oidc`, etc.) et migration vers une nouvelle infrastructure de fragments pour les vues [#859].
- **Optimisation et Traitement** : Amélioration des performances de l'onglet Notification par l'optimisation des requêtes SQL (suppression des requêtes N+1) [#840] et refonte de la logique de traitement des fichiers PDF et des QR codes [#879].

### Autres changements
- Nettoyage du code mort et suppression de dépendances inutilisées [#861].
- Standardisation du formatage des fichiers HTML.

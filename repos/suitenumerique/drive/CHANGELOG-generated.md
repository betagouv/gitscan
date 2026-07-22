## Changelog : drive (30 derniers jours, au 15 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à la recherche de fichiers, avec l'ajout de filtres par type de fichier, contact, date de modification et emplacement. Des corrections de bugs ont également été implémentées pour améliorer la stabilité et la performance, notamment concernant l'indexation par les moteurs de recherche, la gestion des fichiers supprimés et le streaming de fichiers exportés. La sécurité a été renforcée avec la mise à jour de dépendances critiques.

### Évolutions fonctionnelles
- Ajout de filtres de recherche avancés : type de fichier, contact, date de modification et emplacement. [#issue-recherche]
- Amélioration de la recherche dans la corbeille : recherche des éléments racine supprimés.
- Possibilité de convertir un fichier pendant son analyse anti-malware.
- Amélioration de l'interface utilisateur pour les filtres de recherche dans le modal de recherche.
- Ajout d'un menu d'aide dans le panneau latéral gauche.
- Amélioration des tests E2E pour couvrir les nouveaux filtres et fonctionnalités.

### Évolutions techniques
- Mise à jour de la dépendance `PyJWT` et `cryptography` pour corriger des failles de sécurité.
- Optimisation du streaming de fichiers exportés depuis S3 pour éviter la mise en mémoire tampon.
- Refactorisation du code pour améliorer la gestion des filtres d'explorateur.
- Utilisation de composants UI-kit pour les icônes et prévisualisations de fichiers.
- Amélioration de la gestion des requêtes de conversion de fichiers.
- Contrainte de version de `joserfc` pour corriger une vulnérabilité CVE-2026-49852.

### Autres changements
- Amélioration de la documentation README pour plus de clarté.
- Enrichissement des guidelines de contribution.
- Correction de problèmes de tests E2E.
- Suppression de code inutilisé.
- Amélioration des fixtures de démonstration pour le partage de fichiers.

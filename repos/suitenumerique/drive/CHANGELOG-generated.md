## Changelog : drive (30 derniers jours, au 23 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à la gestion du stockage, notamment un indicateur d'utilisation et des limitations configurables. L'expérience utilisateur est également améliorée grâce à de nouveaux filtres de recherche et à une meilleure gestion des quotas. Des corrections de bugs et des mises à jour de dépendances ont également été incluses pour améliorer la stabilité et la sécurité.

### Évolutions fonctionnelles
- Ajout d'un indicateur d'utilisation du stockage et d'un lien vers les paramètres correspondants. [#1234](https://github.com/suitenumerique/drive/issues/1234) (implémentation backend et frontend)
- Amélioration des messages d'erreur liés aux quotas, affichant des informations plus spécifiques.
- Ajout de filtres de recherche avancés : type de fichier, contact, date de modification et emplacement.
- Possibilité de filtrer les résultats de recherche par date de modification (avec des options prédéfinies comme "plus d'un an").
- Ajout d'un menu d'aide dans le pied de page du panneau gauche.
- Amélioration de la recherche de fichiers supprimés dans la corbeille.
- Possibilité de configurer l'ACL (Access Control List) pour les uploads.
- Ajout d'un indicateur visuel pour les contacts partagés dans les filtres de recherche.

### Évolutions techniques
- Mise à jour de plusieurs dépendances : Django, Next.js, Vite, Turbo, pillow, idna, et ui-kit.
- Renforcement de la sécurité en contraignant la version de la librairie `joserfc` pour corriger une vulnérabilité (CVE-2026-49852).
- Amélioration de la gestion des caches de stockage pour une meilleure performance.
- Refactorisation du code pour améliorer la maintenabilité et la lisibilité.
- Amélioration de la gestion des erreurs et des transactions.
- Optimisation de l'exportation de fichiers depuis S3.
- Ajout d'une API pour exposer le quota utilisateur.
- Implémentation d'un backend local pour la gestion des droits d'accès basés sur le stockage.
- Amélioration de la gestion des fichiers supprimés lors de la suppression d'éléments.

### Autres changements
- Mise à jour des tests E2E pour refléter les changements de l'interface utilisateur.
- Correction de fautes d'orthographe dans les messages d'erreur et le code.
- Amélioration de la documentation et des commentaires.
- Suppression de code obsolète.
- Mise à jour de la version de release à 0.20.0.
- Amélioration de la configuration Docker pour une meilleure sécurité.
- Ajout de fixtures pour les tests de démonstration.

## Changelog : drive (30 derniers jours, au 23 juillet 2026)

### Résumé
Cette mise à jour apporte des améliorations significatives à la gestion du quota de stockage des utilisateurs, avec l'ajout d'un indicateur visuel et de messages plus clairs. De plus, des améliorations ont été apportées à la recherche, à la sécurité et à la configuration du système, ainsi qu'à la gestion des fichiers et des permissions.

### Évolutions fonctionnelles
- Ajout d'un indicateur de quota de stockage pour les utilisateurs, affichant l'espace utilisé et disponible. [#2345](https://github.com/suitenumerique/drive/pull/2345)
- Amélioration des messages d'erreur liés au quota dépassé pour une meilleure clarté.
- Possibilité de filtrer les résultats de recherche par date de modification (personnalisable avec un intervalle).
- Ajout de filtres de recherche par type de fichier, contact et emplacement.
- Ajout d'un menu d'aide dans le pied de page du panneau gauche.
- Amélioration de l'expérience utilisateur lors du téléchargement de fichiers avec une notification de progression, d'erreurs et la possibilité d'annulation.

### Évolutions techniques
- Mise à jour de plusieurs dépendances : Django, Next.js, Vite, Turbo, pillow, idna, ui-kit.
- Renforcement de la sécurité en contraignant la version de la librairie joserfc pour corriger une vulnérabilité (CVE-2026-49852).
- Amélioration de la configuration Docker pour une meilleure sécurité et robustesse.
- Optimisation de la gestion du cache de stockage par utilisateur.
- Refactorisation du code pour améliorer la lisibilité et la maintenabilité.
- Exposition de l'information de quota utilisateur via l'API des entitlements.
- Ajout d'un backend local pour la gestion des entitlements avec des limites de stockage.
- Amélioration de la gestion des fichiers supprimés lors du calcul de l'espace de stockage.

### Autres changements
- Ajout de fixtures pour améliorer les tests et la démonstration du système.
- Correction de bugs mineurs dans l'interface utilisateur et les tests.
- Amélioration de la documentation et des messages de log.
- Mise à jour des tests E2E pour refléter les changements de l'interface utilisateur.
- Correction de problèmes liés à l'affichage des icônes et des tests de dropdown.
- Suppression de code obsolète.

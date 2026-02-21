## Changelog : complements-alimentaires (30 derniers jours)

### Résumé
Ce changelog résume les évolutions récentes du projet de gestion des compléments alimentaires. Les dernières semaines ont été marquées par des améliorations significatives en termes d'accessibilité, notamment avec l'ajout de commutateurs pour les cases à cocher et l'amélioration de la navigation au clavier. Des corrections et des améliorations ont également été apportées à l'administration, à la sécurité (CSP) et à l'export des données. Enfin, de nombreuses dépendances ont été mises à jour pour bénéficier des dernières corrections et améliorations de sécurité.

### Évolutions fonctionnelles
- Amélioration de l'accessibilité : remplacement des cases à cocher par des commutateurs pour une meilleure conformité RGAA 11.2 (#2739, #2710).
- Amélioration de l'accessibilité : amélioration de la navigation au clavier et des étiquettes pour les champs de formulaire (#2721, #2723, #2712, #2714, #2715, #2717, #2718, #2719).
- Ajout de la possibilité de modifier les déclarations sans entreprises mandatées (#2734).
- Mise à jour de l'entête des certificats (#2736).
- Ajout de l'entreprise mandatée lors de la duplication d'une déclaration (#2708).
- Inclusion du SIRET et de la TVA dans l'export des données pour les SD (#2683).
- Mise à jour de l'attestation et de l'AR pour les articles 15 (#2703).
- Ajout de l'entreprise mandatée dans l'interface d'administration (#2706).
- Amélioration de la validation automatique des articles 15 (#2702).

### Évolutions techniques
- Mise à jour de la configuration des Content Security Policies (CSP) pour améliorer la sécurité de l'application (#2664, #2656, #2660, #2662, #2663).
- Mise à jour de la base de données PostgreSQL dans les workflows GitHub Actions (#2736).
- Refonte de l'application frontend pour supprimer les styles en ligne et améliorer la maintenabilité (#2663).
- Mise à jour des dépendances Python (Django, cryptography, ipython, etc.) et Node.js (vue, eslint, prettier, etc.) vers leurs dernières versions stables.

### Autres changements
- Ajout du logo du ministère dans les certificats (#2687).
- Amélioration de la documentation et des commentaires dans le code.
- Corrections mineures de l'interface utilisateur et de l'expérience utilisateur.
- Ajout de Metabase dans la liste des domaines autorisés par la CSP (#2700).
- Suppression de l'utilisation de styles inline dans l'application frontend (#2663).
- Amélioration de la gestion des liens de téléchargement (#2674).
- Ajout de tests unitaires et d'intégration.

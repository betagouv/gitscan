## Changelog : egapro (30 derniers jours, au 28 mai 2026)

### Résumé
Les dernières semaines ont été marquées par des améliorations significatives de l'expérience utilisateur, notamment des corrections d'interface et d'alignement avec les maquettes Figma. Des efforts importants ont également été consacrés à l'ajout de nouvelles statistiques et à l'amélioration de l'infrastructure de notification. Enfin, des travaux de fond ont été réalisés sur le cache et la gestion des statuts de la démarche.

### Évolutions fonctionnelles
- Amélioration de l'étape "Quartile" de la déclaration de rémunération avec des corrections visuelles. [#3553](https://github.com/SocialGouv/egapro/issues/3553)
- Alignement de la typographie et du padding du menu "Mon espace" avec les maquettes Figma. [#3525](https://github.com/SocialGouv/egapro/issues/3554)
- Amélioration de l'alignement visuel de différents éléments de l'interface (bannière de ressources, illustration). [#3526](https://github.com/SocialGouv/egapro/issues/3552)
- Ajout de la validation du champ vide et d'une alerte GIP sur l'étape 1 "Effectifs". [#3544](https://github.com/SocialGouv/egapro/issues/3544)
- Désactivation de l'autocomplétion du navigateur sur tous les formulaires pour une meilleure expérience utilisateur. [#3539](https://github.com/SocialGouv/egapro/issues/3548)
- Ajout de nouvelles statistiques :
    - Distribution des scores publics (K7). [#3551](https://github.com/SocialGouv/egapro/issues/3551)
    - Taux d'abandon par étape (K5). [#3218](https://github.com/SocialGouv/egapro/issues/3546)
    - Funnel de complétion (K19). [#3222](https://github.com/SocialGouv/egapro/issues/3545)
    - Taux de déclaration (K1). [#3214](https://github.com/SocialGouv/egapro/issues/3513)
    - Délai moyen par étape (K4). [#3217](https://github.com/SocialGouv/egapro/issues/3521)
- Amélioration de la page récapitulative de la déclaration de rémunération (lecture seule). [#3375](https://github.com/SocialGouv/egapro/issues/3375)
- Ajout de la gestion du statut "annulé" pour les déclarations. [#3431](https://github.com/SocialGouv/egapro/issues/3431)
- Ajout de la gestion des colonnes de pourcentages de la déclaration. [#3405](https://github.com/SocialGouv/egapro/issues/3405)

### Évolutions techniques
- Refactorisation de l'infrastructure de notification pour permettre l'envoi d'emails. [#3466](https://github.com/SocialGouv/egapro/issues/3466)
- Amélioration du système de cache avec une sauvegarde en base de données. [#3537](https://github.com/SocialGouv/egapro/issues/3537)
- Mise en place d'un pipeline de mock GIP-MDS amélioré pour 5 buckets d'effectifs. [#3497](https://github.com/SocialGouv/egapro/issues/3497)
- Amélioration de l'orchestration du pipeline avec correction de bugs et ajout d'observabilité. [#3403](https://github.com/SocialGouv/egapro/issues/3403)
- Correction d'un bug lié à la migration silencieuse des données. [#3559](https://github.com/SocialGouv/egapro/issues/3559)
- Correction de bugs et améliorations de l'orchestration du pipeline. [#3423](https://github.com/SocialGouv/egapro/issues/3423)
- Amélioration de la gestion des statuts de la démarche. [#3457](https://github.com/SocialGouv/egapro/issues/3457)

### Autres changements
- Documentation de l'architecture et des fonctionnalités de la V2 d'EgaPro. [#3390](https://github.com/SocialGouv/egapro/issues/3390), [#3389](https://github.com/SocialGouv/egapro/issues/3389)
- Amélioration de la documentation des parcours utilisateurs. [#3391](https://github.com/SocialGouv/egapro/issues/3391)
- Correction de problèmes d'alignement et de style sur différentes pages (Mon espace, login, étapes de déclaration). [#3344](https://github.com/SocialGouv/egapro/issues/3340), [#3371](https://github.com/SocialGouv/egapro/issues/3370), [#3361](https://github.com/SocialGouv/egapro/issues/3360)
- Suppression de Seuil_Q4_* de l'API SUIT suite à une migration. [#3493](https://github.com/SocialGouv/egapro/issues/3493)
- Ajout de tests et d'améliorations de la configuration du pipeline CI/CD. [#3408](https://github.com/SocialGouv/egapro/issues/3408)
- Correction de liens et de routes pour les statuts de la démarche. [#3485](https://github.com/SocialGouv/egapro/issues/3485)

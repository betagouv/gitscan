## Changelog : egapro (30 derniers jours, au 2026-06-17)

### Résumé
Les dernières semaines ont été marquées par des améliorations significatives de l'expérience utilisateur, notamment dans les parcours de déclaration et de mise en conformité, avec un alignement plus précis sur les maquettes Figma. Des efforts ont également été déployés pour améliorer la performance et la stabilité de la plateforme, ainsi que pour enrichir les statistiques disponibles pour l'administration. Enfin, l'infrastructure de notification par email a été revue et corrigée.

### Évolutions fonctionnelles
- Amélioration de l'alignement visuel de la page de récapitulatif de la seconde déclaration, masquant certains éléments conditionnels et ajustant le titre et le bouton. [#3582](https://github.com/SocialGouv/egapro/issues/3582) [#3653]
- Corrections visuelles et amélioration du focus sur l'ajout d'informations à l'étape 5 du parcours de déclaration. [#3538](https://github.com/SocialGouv/egapro/issues/3538) [#3589]
- Amélioration de l'étape 6 du parcours de revue, avec un changement de couleur et un ajustement de la graisse de la police. [#3540](https://github.com/SocialGouv/egapro/issues/3540) [#3588]
- Intégration de l'historique des statuts dans l'application, permettant de suivre l'évolution des déclarations. [#3584](https://github.com/SocialGouv/egapro/issues/3584) [#3611]
- Correction des URLs des emails de notification et refactorisation du système de templates. [#3606]
- Affichage du récapitulatif de la déclaration sur la page de détail de l'administration. [#3437](https://github.com/SocialGouv/egapro/issues/3437) [#3590]
- Amélioration de la validation du champ vide et ajout d'une alerte GIP sur l'étape 1 du parcours de déclaration. [#3544]
- Désactivation de l'autocomplétion du navigateur sur tous les formulaires pour une meilleure expérience utilisateur. [#3539](https://github.com/SocialGouv/egapro/issues/3539) [#3548]
- Ajout de nouvelles statistiques : taux de déclaration, délai moyen par étape, distribution des scores publics, taux d'abandon par étape et funnel de complétion. [#3214](https://github.com/SocialGouv/egapro/issues/3214) [#3513], [#3217](https://github.com/SocialGouv/egapro/issues/3217) [#3521], [#3218](https://github.com/SocialGouv/egapro/issues/3218) [#3546], [#3222](https://github.com/SocialGouv/egapro/issues/3222) [#3545], [#3551]
- Exposition de l'ID de déclaration dans l'API SUIT. [#3478](https://github.com/SocialGouv/egapro/issues/3478) [#3481]

### Évolutions techniques
- Implémentation d'un plan de tracking Matomo pour les événements client et la documentation. [#3625]
- Refonte des pages d'avis du CSE. [#3476](https://github.com/SocialGouv/egapro/issues/3476) [#3639]
- Ajout d'un agent tu-dev pour l'écriture de tests unitaires et d'intégration. [#3620]
- Refactorisation du système de cache avec une sauvegarde en base de données. [#3484](https://github.com/SocialGouv/egapro/issues/3484) [#3537]
- Extraction du kit de templates React Email pour une meilleure organisation et réutilisabilité. [#3561]
- Amélioration de l'orchestration avec l'ajout d'outils de planification et de suivi de la vélocité. [#3644]
- Suppression des tests E2E lors de la fusion des fonctionnalités épiques pour optimiser le CI/CD. [#3635]
- Correction d'un problème de blocage de l'installation de Playwright dans le CI/CD. [#3591]

### Autres changements
- Découplage du draft read de la date limite de la campagne. [#3594](https://github.com/SocialGouv/egapro/issues/3594) [#3656]
- Ajustement de l'alignement du CompanyBanner avec les maquettes Figma. [#3532](https://github.com/SocialGouv/egapro/issues/3532) [#3573]
- Correction de l'affichage des étiquettes de champs de formulaire pour la conformité RGAA.
- Correction de bugs mineurs liés à l'affichage et au comportement de l'interface utilisateur, notamment l'alignement des éléments et la gestion des erreurs.
- Correction de la route du bouton précédent sur la page d'avis du CSE. [#3485]
- Correction de l'affichage des labels d'étape pour les statuts du parcours de conformité. [#3495]
- Suppression des seuils Q4 de l'API SUIT suite à une migration. [#3493]
- Correction du nom de la phase 2 en "processus de conformité" dans l'API SUIT. [#3496]
- Amélioration de la gestion des dates dans l'API SUIT. [#3486]

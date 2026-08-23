## Changelog : lab-anssi-ui-kit (30 derniers jours, au 21 août 2026)

### Résumé
Cette période a été marquée par l'enrichissement de la bibliothèque avec l'ajout de nouveaux composants et une mise en conformité majeure de plusieurs éléments existants avec le DSFR (Design System de l'État). Un effort important a également été porté sur l'accessibilité, la réactivité (responsive) et la flexibilité de personnalisation des composants pour les développeurs.

### Évolutions fonctionnelles
- **Nouveaux composants** : Ajout du composant `LabAnssiFonctionnalites` (Bloc Fonctionnalités) et du `DsfrTooltip`.
- **Accessibilité** : 
    - Intégration du support `prefers-reduced-motion` et ajout d'un bouton de pause pour le défilement automatique dans `LabAnssiFonctionnalites`.
    - Ajout de la directive `trapFocus` pour le composant `DsfrModal`.
- **Personnalisation accrue** :
    - Ajout de slots média (`media-{id}`) pour personnaliser les zones d'illustration dans `LabAnssiFonctionnalites`.
    - Nouvelles propriétés de personnalisation pour les thèmes, les couleurs et le z-index (notamment pour `BandeauPage`, `SuiteCyber` et `LabAnssiCentreAide`).
    - Ajout de la propriété `noIcon` sur `DsfrCard`.
- **Améliorations de l'expérience utilisateur** :
    - Optimisation du comportement responsive (points de rupture et tailles de texte) pour `LabAnssiCentreAide`, `LabAnssiCarrouselTuiles`, `BandeauPage` et `PresentationANSSI`.
    - Corrections de bugs d'affichage sur mobile pour `SuiteCyber` et `LabAnssiCentreAide`.

### Évolutions techniques
- **Conformité DSFR** : Refonte structurelle et stylistique de plusieurs composants (`SuiteCyber`, `LabAnssiCentreAide`, `LabAnssiCarrouselTuiles` et `LabAnssiMarelle`) pour garantir un alignement strict avec les standards du DSFR.
- **Refactoring** : 
    - Remplacement des couleurs codées en dur par des variables CSS pour faciliter la maintenance et la personnalisation.
    - Unification des valeurs de `z-index` pour éviter les conflits d'affichage.
- **Outils et Infrastructure** :
    - Mise à jour de Storybook vers la version 10.5.8.
    - Application de politiques de cache lors de l'envoi des assets vers S3.
    - Correction de scripts liés aux types MIME.

### Autres changements
- **Documentation** : Correction de l'affichage des couleurs de fond personnalisées dans la documentation du composant `BandeauPage`.
- **Organisation** : Réorganisation de Storybook avec le déplacement des stories du LAB vers un dossier "legacy".

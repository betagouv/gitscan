## Changelog : lab-anssi-ui-kit (30 derniers jours, au 15 septembre 2026)

### Résumé
Cette période est marquée par une montée en maturité technique et une meilleure conformité aux standards du DSFR. Les évolutions se concentrent sur la réactivité des composants, l'amélioration de l'accessibilité et une mise à jour majeure de l'infrastructure de build (passage à Vite 8). Les utilisateurs bénéficieront d'une interface plus fluide et mieux adaptée aux mobiles, notamment sur les composants de la gamme "Lab".

### Évolutions fonctionnelles
- **Nouveaux composants et fonctionnalités** :
    - Ajout du composant `DsfrShare`.
    - Ajout d'un slot d'indication (`hint`) pour le composant `DsfrToggle`.
    - Amélioration du composant `LabAnssiFonctionnalites` : ajout d'un bouton pause, support du mode "réduction de mouvement" et nouveaux slots pour personnaliser les zones de médias.
- **Accessibilité (A11y)** :
    - Amélioration de la visibilité du focus.
    - Nommage des boutons de fermeture (composant Alerte) pour les lecteurs d'écran.
    - Optimisation des rôles ARIA sur les groupes de boutons, de cases à cocher et de radios pour éviter les redondances.
- **Améliorations de l'interface (UI/UX)** :
    - **Responsive** : Optimisation des tailles (icônes, titres, boutons) et des espacements pour une meilleure adaptation mobile sur `LabAnssiCentreAide`, `LabAnssiSuiteCyber`, `LabAnssiBandeauPage` et `PresentationANSSI`.
    - **Corrections visuelles** : Correction de l'alignement du `DsfrDropdown`, de l'affichage du `LabAnssiBandeauPage` en mode sans image, et de la gestion des couleurs de thèmes pour `SuiteCyber`.

### Évolutions techniques
- **Infrastructure de build** :
    - Migration majeure vers **Vite 8**, incluant le passage au format ESM et la correction de l'injection du nonce CSP.
    - Consolidation de la configuration `pnpm` et utilisation systématique du lockfile.
- **Qualité et robustesse** :
    - Intégration de `svelte-check` pour renforcer la vérification des types.
    - Mise à jour de la `peerDependency` Svelte vers `^5.55.0`.
    - Correction de violations de politique de sécurité (CSP) dans le header.
- **Réactivité des composants** :
    - Refonte interne pour rendre de nombreux composants plus réactifs et assurer une synchronisation parfaite des états (notamment pour `DsfrTranslate`, `DsfrTable`, `MultiSelect`, `DsfrSegmented` et `LienDiagnosticCyber`).

### Autres changements
- **Storybook** : Mise en conformité des stories avec les standards ISO DSFR et correction des chemins d'images.
- **Nettoyage** : Suppression de blocs de code et de styles "legacy" dans les composants `CentreAide` et `PageCrisp`.
- **Documentation** : Mise à jour de la description du processus de release.

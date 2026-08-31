## Changelog : lab-anssi-ui-kit (30 derniers jours, au 27 août 2026)

### Résumé
Cette période a été marquée par une montée en version majeure de l'infrastructure de build (passage à Vite 8) et une série d'améliorations visant à renforcer la conformité au DSFR, l'accessibilité et la réactivité des composants. Le kit gagne en maturité avec l'ajout de nouveaux composants et une meilleure gestion des états dynamiques.

### Évolutions fonctionnelles

**Nouveautés et fonctionnalités**
- Ajout du composant `Bloc Fonctionnalités`.
- Ajout de nouveaux slots pour augmenter la personnalisation : `hint` pour `DsfrToggle` et `afternavigation` pour `DsfrHeader`.
- Introduction de la propriété `noIcon` sur `DsfrCard` pour masquer l'icône du lien.
- Ajout de la gestion du mode `prefers-reduced-motion` et d'un bouton de pause pour le composant `LabAnssiFonctionnalites`.

**Accessibilité et conformité**
- Mise en conformité de plusieurs composants (`SuiteCyber`, `LabAnssiCentreAide`) avec les standards du DSFR.
- Amélioration de l'accessibilité : nommage des boutons de fermeture pour les alertes et suppression de rôles ARIA redondants sur les groupes de boutons/cases à cocher.
- Documentation des tags pressables pour une meilleure compréhension de l'interaction.

**Améliorations de l'expérience utilisateur (UI/UX)**
- **Réactivité accrue** : Synchronisation des valeurs et des états pour de nombreux composants (MultiSelect, DsfrSegmented, DsfrTable, DsfrTranslate, etc.).
- **Ajustements visuels** : Optimisation des points de rupture (breakpoints) pour `BandeauPage` et `CarrouselTuiles`, et ajustement des tailles d'icônes et de titres selon la résolution.
- **Gestion des couches** : Uniformisation et ajustement des `z-index` pour éviter les conflits d'affichage (notamment pour le Centre d'Aide).

### Évolutions techniques

**Infrastructure et Build**
- Migration majeure vers **Vite 8**, incluant le passage aux modules ESM et la correction de l'injection du nonce CSP.
- Consolidation de la configuration `pnpm`.
- Optimisation du déploiement vers S3 avec l'application de politiques de cache et la correction des types MIME.
- Mise à jour de la configuration Storybook.

**Refactoring et Optimisation**
- Nettoyage de la base de code par la suppression de blocs de code et d'effets "legacy" (notamment dans `CentreAide` et `PageCrisp`).
- Remplacement des couleurs codées en dur par des variables CSS pour une meilleure maintenabilité.

### Autres changements
- **Documentation** : Mise à jour de la documentation pour `DsfrTagsGroup` et `LabAnssiBandeauPage`.
- **Qualité de code** : Mise à jour du formatage global du projet suite à la montée de version de Prettier.

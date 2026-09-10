## Changelog : lab-anssi-ui-kit (30 derniers jours, au 09/09/2026)

### Résumé
Cette période a été marquée par un effort important de mise en conformité avec les standards du DSFR et une amélioration significative de l'accessibilité. Les composants ont été rendus plus réactifs et dynamiques, tandis que plusieurs éléments de l'interface (notamment les composants du Lab ANSSI) ont été affinés pour offrir une meilleure expérience sur mobile et une gestion plus fine des interactions (mouvements, focus, z-index).

### Évolutions fonctionnelles
- **Nouveautés** :
    - Ajout du composant `DsfrShare`.
- **Accessibilité** :
    - Amélioration de la visibilité du focus pour une meilleure navigation au clavier.
    - Support du paramètre `prefers-reduced-motion` pour le composant `LabAnssiFonctionnalites`, incluant un bouton de pause pour le défilement automatique.
    - Correction des rôles ARIA redondants sur les groupes de boutons (`DsfrRadiosGroup`, `DsfrCheckboxesGroup`).
    - Nommage explicite du bouton de fermeture dans le composant `Alerte`.
- **Réactivité et synchronisation** :
    - Mise en place de la réactivité pour de nombreux composants : état `disabled` (DSFR), langue active (`DsfrTranslate`), pagination (`DsfrTable`), valeurs sélectionnées (`MultiSelect`, `DsfrSegmented`), et attributs de liens (`LienDiagnosticCyber`).
- **Améliorations de l'interface (UI/UX)** :
    - **Gestion des icônes** : Possibilité de surcharger la taille des icônes, compatibilité accrue avec les styles DSFR et masquage intelligent de l'icône "blank".
    - **Responsive Design** : Ajustement des points de rupture (breakpoints) et de la taille des éléments pour `LabAnssiBandeauPage`, `LabAnssiCentreAide` et `LabAnssiCarrouselTuiles`.
    - **Personnalisation** : Ajout de nouveaux slots pour permettre une personnalisation accrue (`DsfrToggle`, `DsfrHeader`, `LabAnssiFonctionnalites`).
    - **Correction de bugs** : Résolution de problèmes d'affichage sur mobile pour `LabAnssiBandeauPage` et `SuiteCyber`.

### Évolutions techniques
- **Infrastructure et Outillage** :
    - Migration majeure vers **Vite 8**, incluant le passage aux modules ESM et la correction de l'injection du nonce CSP.
    - Consolidation de la configuration `pnpm` et utilisation systématique du lockfile.
    - Intégration de `svelte-check` pour renforcer la vérification des types lors du développement.
- **Sécurité** :
    - Correction d'une violation de la politique de sécurité du contenu (CSP) au niveau de la navigation du header.
- **Qualité et Refactoring** :
    - Refactorisation profonde de plusieurs composants (`CentreAide`, `SuiteCyber`, `PageCrisp`) pour supprimer le code legacy et garantir une structure strictement conforme au DSFR.
    - Élargissement de la dépendance Svelte pour supporter les versions supérieures (^5.55.0).

### Autres changements
- **Storybook** : Réorganisation des stories du LAB (déplacement vers un dossier legacy) et mise en conformité des exemples avec les standards ISO DSFR.
- **Documentation** : Mise à jour de la description du processus de publication (release).

## Changelog : lab-anssi-ui-kit (30 derniers jours, au 31 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à la compatibilité avec le Design System de la République Française (DSFR), notamment avec l'ajout de nouveaux composants (DsfrTooltip, DsfrModal) et l'amélioration de composants existants (CarrouselTuiles, Marelle, DsfrButton). Des optimisations de performance et des corrections de sécurité ont également été implémentées. Enfin, l'organisation des stories dans Storybook a été revue pour une meilleure expérience développeur.

### Évolutions fonctionnelles
- Ajout du composant `DsfrTooltip` pour afficher des infobulles d'aide.
- Ajout du composant `DsfrModal` avec implémentation du "trapFocus" pour une meilleure accessibilité.
- Le composant `LAB - CarrouselTuiles` est maintenant compatible avec le DSFR.
- Le composant `LAB - Marelle` est maintenant compatible avec le DSFR.
- Ajout de variations inversées tertiaires et tertiaires sans bordure au composant `DsfrButton`.
- Amélioration de la directive permettant d'implémenter le 'trapFocus' pour une meilleure gestion du focus dans les modales.
- Le label du bouton du composant `DsfrCallout` est maintenant optionnel.
- Ajout de l'attribut `hide-label` à la story du composant `DsfrSelect` pour plus de flexibilité.
- Ajout de l'attribut `disabled` au lien du composant `DsfrConnect`.
- Définition de la valeur par défaut de la prop 'groupMarkup' du composant `DsfrTagsGroup`.
- Ajout de boutons inversés aux stories du composant `LabAnssiBandeauPage` dans Storybook.
- Les étapes du composant `Marelle` sont maintenant plus facilement personnalisables grâce à l'ajout de slots.

### Évolutions techniques
- Mise à jour de Storybook vers la version 10.5.0.
- Optimisation du composant `DsfrSegmented` avec l'utilisation de `requestAnimationFrame` pour améliorer la performance du `ResizeObserver`.
- Mise à jour de PNPM vers la version 11.17.0 pour bénéficier des dernières corrections et améliorations.
- Fixe de la version de Node.js à la dernière version LTS (24.18.0) pour assurer la stabilité et la sécurité.
- Ajout de la configuration `allowBuilds` pour `@parcel/watcher` et `esbuild` dans `pnpm-workspace.yaml`.
- Mise à jour de la configuration de Renovate pour inclure des règles de groupe et des préfixes de commit.
- Ajout de la configuration pour Code Connect (Figma).
- Améliorations de la sécurité du CI :
    - Évite les injections dans le CI.
    - Désactive les identifiants `git` des dépôts clônés.
    - Ajout de `checkov` et `zizmor` pour valider la configuration.

### Autres changements
- Réorganisation des titres des composants Lab ANSSI et DSFR dans Storybook.
- Suppression des options de tri des stories dans Storybook.
- Passage à la version 1.57.0, 1.56.0 et 1.55.2.
- Mise à jour de diverses dépendances (eslint, postcss, playwright, style-dictionary, svelte, etc.).
- Mise à jour des actions GitHub (actions/checkout, actions/setup-node, actions/upload-pages-artifact, actions/deploy-pages, github/codeql-action, s3-actions/s3cmd, bridgecrewio/checkov-action, zizmorcore/zizmor-action).

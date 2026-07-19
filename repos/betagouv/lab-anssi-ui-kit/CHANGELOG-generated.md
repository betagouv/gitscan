## Changelog : lab-anssi-ui-kit (30 derniers jours, au 17 juillet 2026)

### Résumé
Cette nouvelle version apporte des améliorations de stabilité et de sécurité, ainsi que des évolutions sur les composants DSFR, notamment en termes d'accessibilité et de personnalisation. Des optimisations ont été apportées à certains composants pour améliorer leur flexibilité et leur intégration. L'outillage de CI/CD a également été renforcé avec l'ajout d'analyse de sécurité.

### Évolutions fonctionnelles
- **DsfrToggle :** Ajout d'une propriété `hideLabel` pour masquer le label et correction de l'affichage de l'état "checked".
- **DsfrDropdown :** Correction de l'alignement à droite du menu déroulant.
- **DsfrRange :** Ajout de la prise en charge de `box-sizing`.
- **DsfrTabnav :** Ajout de la prise en charge de `createSlot` pour les liens du composant.
- **DsfrLabel :** Ajout du composant `DsfrLabel` et remplacement de l'utilisation directe de la balise `<label>` par ce composant dans d'autres composants.
- **DsfrCheckboxesGroup & DsfrRadiosGroup :** Ajout de la prise en charge de la taille et de la graisse pour les légendes.
- **DsfrLabel :** Ajout de la prise en charge de la taille et de la graisse.
- **Marellement :** Les étapes sont maintenant plus facilement personnalisables grâce à l'utilisation de slots.

### Évolutions techniques
- **Sécurité CI/CD :** Ajout d'outils d'analyse de sécurité (`checkov` et `zizmor`) pour valider la configuration et éviter les injections. Désactivation des identifiants `git` des dépôts clonés pour renforcer la sécurité.
- **Renovate :** Mise en place et configuration de Renovate pour la gestion automatisée des dépendances et des actions CI/CD.
- **Optimisation DsfrSegmented :** Optimisation du `ResizeObserver` avec `requestAnimationFrame` pour améliorer les performances.
- **Mise à jour des dépendances :** Plusieurs dépendances ont été mises à jour (Svelte, TypeScript, Vitest, Storybook, etc.).
- **CI :** Mise à jour de l'étape de checkout pour utiliser la référence du dépôt et un `fetch-depth` de 0.

### Autres changements
- **Storybook :** Réorganisation des titres des composants Lab ANSSI et DSFR dans Storybook. Suppression des options de tri des stories.
- **Documentation :** Amélioration de l'organisation des stories d'exemples.
- **Configuration :** Mise à jour du fichier `renovate.json`.
- **Version :** Passage aux versions 1.55.2, 1.55.1, 1.55.0 et 1.54.2, 1.54.1, 1.54.0.

## Changelog : lab-anssi-ui-kit (30 derniers jours, au 23 juillet 2026)

### Résumé
Cette version apporte des améliorations à plusieurs composants, notamment DsfrConnect, DsfrTagsGroup, DsfrCallout, DsfrSelect, DsfrSegmented et DsfrTabnav, en ajoutant de nouvelles options de configuration et en corrigeant des bugs d'affichage. Des mises à jour de dépendances et des améliorations de la sécurité du CI ont également été implémentées. Enfin, l'organisation des stories dans Storybook a été revue pour une meilleure clarté.

### Évolutions fonctionnelles
- **DsfrConnect:** Ajout de l'attribut `disabled` au lien du composant, permettant de le désactiver.
- **DsfrTagsGroup:** Définition d'une valeur par défaut pour la prop `groupMarkup`.
- **DsfrCallout:** Le label du bouton est maintenant optionnel.
- **DsfrSelect:** Ajout de l'attribut `hide-label` à la story du composant, permettant de masquer le label.
- **DsfrToggle:** Ajout de la propriété `hideLabel` pour masquer le label et correction de l'affichage de l'état "checked".
- **DsfrDropdown:** Correction de l'alignement à droite du menu déroulant.
- **DsfrTabnav:** Ajout de la prise en charge de `createSlot` pour les liens du composant.
- **DsfrRange:** Ajout de la prise en charge de `box-sizing`.
- **DsfrLabel, DsfrCheckboxesGroup & DsfrRadiosGroup:** Ajout de la prise en charge de la taille et de la graisse pour les légendes et les labels. Remplacement de l'usage de la balise `<label>` par le composant `DsfrLabel`.
- **Marello:** Les étapes sont maintenant plus facilement personnalisables grâce à l'ajout de slots.

### Évolutions techniques
- **Sécurité CI:** Ajout de `checkov` et `zizmor` pour valider la configuration et correction de failles potentielles (injection, identifiants git).
- **Storybook:** Réorganisation des titres des composants Lab ANSSI et DSFR, suppression des options de tri des stories.
- **Performance:** Optimisation du `ResizeObserver` dans le composant `DsfrSegmented` avec `requestAnimationFrame`.
- **Dépendances:** Mise à jour de nombreuses dépendances (Storybook, Svelte, ESLint, Vitest, etc.).
- **Renovate:** Ajout et configuration de Renovate pour la gestion automatisée des dépendances.

### Autres changements
- **Documentation:** Amélioration de l'organisation des stories d'exemples.
- **Version:** Passage aux versions 1.55.2, 1.55.1, 1.55.0, 1.54.2, 1.54.1.
- **Configuration:** Mise à jour du formattage du fichier `renovate.json`.
- **CI:** Mise à jour de l'étape de checkout pour utiliser la référence du dépôt et un fetch-depth de 0.

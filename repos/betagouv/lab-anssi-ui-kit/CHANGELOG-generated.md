## Changelog : lab-anssi-ui-kit (30 derniers jours, au 7 mai 2026)

### Résumé
Cette version apporte des améliorations significatives à la thématisation, à la gestion des formulaires et aux composants Header et Navigation. Des corrections de bugs et des optimisations ont également été apportées, notamment concernant la validation HTML, les onglets et les badges. L'ajout de nouveaux composants comme User et MessagesGroup enrichit la bibliothèque.

### Évolutions fonctionnelles
- **Thématisation :** Ajout d'un paramètre pour activer ou désactiver la thématisation des composants. Documentation ajoutée expliquant comment désactiver la thématisation.
- **Formulaires :** Implémentation de la validation des contraintes HTML pour les composants DsfrCheckbox, DsfrCheckboxesGroup, DsfrInput, DsfrSelect, DsfrSearch, DsfrTextarea et DsfrRadiosGroup. Association des composants DSFR aux formulaires web natifs.
- **Header :** Ajout de slots pour personnaliser la barre de navigation et les liens d'outils du composant DsfrHeader. Ajout d'exemples de Header pour MQC et MSS (connectés et non connectés). Gestion des ToolLinks via une prop dédiée.
- **Navigation :** Amélioration de la gestion des sous-menus du composant DsfrNavigation. Modification de la structure de MenuItem. Correction de l'affichage du statut "actif" des sous-items.
- **Nouveaux composants :** Ajout des composants DsfrUser et DsfrMessagesGroup.
- **Badges :** Ajout du type et du statut aux badges du composant DsfrBadgesGroup.
- **Tabs :** Amélioration du mode de calcul de la hauteur des onglets du composant DsfrTabs.
- **Cards :** Ajout d'un slot pour insérer une image personnalisée dans le composant DsfrCard. Inversion de la position du slot 'contentend'.
- **Buttons :** Rendre la prop 'label' du bouton optionnel.

### Évolutions techniques
- **Sécurité :** Application d'un patch de sécurité concernant 'follow-redirects'.
- **Refactoring :** Extraction de la logique de validation dans une fonction externe pour améliorer la réutilisabilité.
- **Mises à jour :** Mise à jour des dépendances obsolètes.
- **Storybook :** Organisation des exemples pour la carte de jeu. Ajout d'exemples pour DsfrTabs avec un système de notifications et pour le Header. Suppression de l'exemple de LandingMAC.
- **Styles :** Ajout de styles de fallback pour le conteneur dsfr.

### Autres changements
- Amélioration de la lisibilité des descriptions des slots dans les stories.
- Ajout des descriptions des slots dans les stories.
- Correction du wording du bouton "Diagnostic".
- Modification des breakpoints de la NavigationSuiteCyber.
- Ajout de la gestion de l'héritage de la police dans les éléments button et select.
- Correction de l'application du disabled sur les input du composant DsfrRadiosGroup.
- Correction du passage de la prop 'inline' au composant DsfrButtonsGroup dans Storybook.
- Ajout d'une story d'exemple pour la validation des formulaires.
- Ajout d'une story d'exemple du Header MSS (connecté).
- Ajout d'une story d'exemple du Header MSS (non connecté).
- Modification du passage des tools links en JSON dans le composant DsfrHeader.
- Ajout de la gestion des variations 'buttons' et 'links' du composant.

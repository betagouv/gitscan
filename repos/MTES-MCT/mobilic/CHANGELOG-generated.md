## Changelog : mobilic (30 derniers jours, au 16 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur, notamment dans l'interface d'administration et lors de la saisie des missions. Des corrections de bugs et des optimisations de performance ont également été apportées, en particulier au niveau de l'affichage des données sur la page d'accueil de l'administration. L'ajout de la recherche Natinf est une nouvelle fonctionnalité importante.

### Évolutions fonctionnelles
- Ajout d'une recherche Natinf pour faciliter l'accès aux informations. [#861](https://github.com/MTES-MCT/mobilic/pull/861)
- Amélioration de l'interface pour la gestion des infractions dans l'espace administrateur, avec une meilleure organisation et une expérience utilisateur plus fluide. [#860](https://github.com/MTES-MCT/mobilic/pull/860)
- Le bouton "Conduire" est renommé "Travail" lorsque d'autres tâches sont désactivées, pour une meilleure clarté. [#871](https://github.com/MTES-MCT/mobilic/pull/871)
- Ajout d'un logo Chaventon Express. [#848](https://github.com/MTES-MCT/mobilic/pull/848)
- Mise à jour du texte de la page sécurité. [#850](https://github.com/MTES-MCT/mobilic/pull/850)
- Correction de l'affichage du champ "Conducteur" en dehors du mode équipe. [#875](https://github.com/MTES-MCT/mobilic/pull/875)
- Correction pour permettre la sélection de "Accompagnement" dans le menu déroulant. [#872](https://github.com/MTES-MCT/mobilic/pull/872)
- Correction pour que les paramètres de l'entreprise soient respectés au lieu de toujours utiliser la valeur par défaut. [#872](https://github.com/MTES-MCT/mobilic/pull/872)
- Correction pour afficher le libellé "Conduite" en mode accompagnement. [#872](https://github.com/MTES-MCT/mobilic/pull/872)
- Correction pour rafraîchir les données après la validation d'une mission dans le panneau de validation administrateur. [#873](https://github.com/MTES-MCT/mobilic/pull/873)
- Correction pour le téléchargement de l'historique du contrôleur C1B. [#857](https://github.com/MTES-MCT/mobilic/pull/857)
- Correction pour les longues pauses (NATINF_32083). [#843](https://github.com/MTES-MCT/mobilic/pull/843)
- Correction de l'agrégation des données du tableau de temps de travail dans les vues hebdomadaires et mensuelles. [#844](https://github.com/MTES-MCT/mobilic/pull/844)
- Correction du format de date pour l'export C1B. [#853](https://github.com/MTES-MCT/mobilic/pull/853)
- Amélioration de la documentation du contrôleur et des liens vers les vidéos. [#853](https://github.com/MTES-MCT/mobilic/pull/853)

### Évolutions techniques
- Refactor de la gestion des labels réglementaires pour réutiliser les constantes. [#842](https://github.com/MTES-MCT/mobilic/pull/842)
- Optimisation des requêtes sur la page d'accueil de l'administration pour améliorer les performances, en limitant la requête au semaine courante. [#865](https://github.com/MTES-MCT/mobilic/pull/865)
- Refactor de composants pour supprimer les duplications (AccordionActions). [#850](https://github.com/MTES-MCT/mobilic/pull/850)
- Remplacement des icônes MUI par des icônes DSFR dans les composants d'infraction. [#850](https://github.com/MTES-MCT/mobilic/pull/850)
- Utilisation de `Number.parseInt` au lieu de `parseInt`. [#850](https://github.com/MTES-MCT/mobilic/pull/850)
- Suppression de variables et d'imports inutilisés. [#848](https://github.com/MTES-MCT/mobilic/pull/848)

### Autres changements
- Correction de fautes de frappe dans la documentation. [#871](https://github.com/MTES-MCT/mobilic/pull/871)
- Amélioration de la documentation de la page du contrôleur. [#863](https://github.com/MTES-MCT/mobilic/pull/863)
- Corrections de typographie et de formulation sur la page d'accueil de l'administration. [#851](https://github.com/MTES-MCT/mobilic/pull/851) et [#856](https://github.com/MTES-MCT/mobilic/pull/856)
- Ajout d'un bouton de soumission fixe en bas du résumé de la mission. [#868](https://github.com/MTES-MCT/mobilic/pull/868)
- Correction de l'affichage du bouton "Drive" lorsqu'une autre tâche est désactivée. [#855](https://github.com/MTES-MCT/mobilic/pull/855)

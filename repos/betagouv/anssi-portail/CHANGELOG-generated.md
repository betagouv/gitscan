## Changelog : anssi-portail (30 derniers jours, au 28 juillet 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la performance du site via le rendu côté serveur (SSR) et la mise à jour de l'interface utilisateur (UI) avec les nouveaux composants de design. Des corrections et améliorations ont également été apportées à la navigation, à la sécurité et à la gestion des données.

### Évolutions fonctionnelles
- Implémentation du rendu côté serveur (SSR) pour plusieurs pages : accueil, financements, collectivités, associations, NIS2, sessions de groupe, guides et catalogue. Cela devrait améliorer la vitesse de chargement et l'accessibilité du site.
- Ajout d'un export CSV des mesures du parcours de sécurisation.
- Amélioration de l'affichage et de la navigation dans le parcours de sécurisation, notamment avec l'ajout d'une barre de progression et la gestion des modules.
- Mise à jour des filtres et de l'affichage des mesures dans le parcours de sécurisation.
- Ajout de tutoriels pour les mesures du parcours de sécurisation.
- Modification de l'affichage du titre de page et de la carte d'une mesure dans le parcours de sécurisation.
- Amélioration de l'affichage des badges et des collections de guides.
- Correction de l'affichage d'un espace insécable.
- Mise à jour du wording des CTA du parcours de sécurisation.

### Évolutions techniques
- Migration vers Svelte 5 pour le composant Guide.
- Refonte de l'architecture pour supporter le rendu côté serveur (SSR) avec une séparation claire des composants client et serveur.
- Utilisation d'un enrichisseur Svelte pour le SSR.
- Mise à jour de plusieurs dépendances, notamment `axios`, `eslint`, `sharp`, `dompurify`, `vitest`, `prettier-plugin-svelte` et `papaparse`.
- Amélioration de la configuration CI/CD avec la gestion des secrets et l'ajout d'outils de sécurité comme `zizmor`.
- Ajout d'un Nix Shell pour faciliter le développement en local.
- Uniformisation des versions de dépendances.
- Utilisation de UUID v7 pour générer des clés primaires.

### Autres changements
- Ajout des métadonnées Open Graph et Twitter pour améliorer le partage sur les réseaux sociaux.
- Correction de liens et de styles divers.
- Nettoyage de code et suppression de configurations inutiles.
- Mise à jour de la documentation et du README.
- Ajout de tests et corrections de bugs mineurs.
- Ajout de la campagne Matomo à l'origine des demandes d'aide.
- Correction de l'URL canonique pour inclure le `site.url`.
- Suppression d'un test obsolète.
- Ajout de la taille sur toutes les images.

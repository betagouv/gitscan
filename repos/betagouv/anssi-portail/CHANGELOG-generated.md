## Changelog : anssi-portail (30 derniers jours, au 5 juin 2026)

### Résumé
Ce mois-ci, l'ANSSI-portail a connu une importante évolution avec l'adoption massive des composants du Design System Français (DSFR) pour une interface plus cohérente et accessible.  Des améliorations ont également été apportées au parcours de sécurisation, aux mesures de sécurité, et à la gestion des erreurs, tout en renforçant la sécurité globale de la plateforme.

### Évolutions fonctionnelles
- Intégration des composants DSFR sur de nombreuses pages : accueil, services, parcours, catalogue, guides, connexions, favoris, maintenance, etc. pour une expérience utilisateur plus harmonieuse.
- Amélioration de la page 404 pour une meilleure expérience en cas d'erreur.
- Affichage de la progression dans le parcours de sécurisation, avec l'utilisation d'un composant de progression dédié.
- Affichage des cartes des mesures de sécurité dans le parcours de sécurisation.
- Affichage des mesures de sécurité avec des informations détaillées (risques, actions prioritaires, liens utiles, exigences ReCyF).
- Correction de l'affichage des erreurs lors d'une demande de diagnostic.
- Ajout d'un encart d'information sur la page d'accueil pour le diagnostic.
- Possibilité de filtrer les collections dans le catalogue.
- Amélioration de la validité du numéro de téléphone lors de l'inscription.
- Possibilité de désactiver la validation du SIRET.
- Ajout d'un composant de contrôle segmenté pour améliorer l'expérience utilisateur.

### Évolutions techniques
- Mise à jour de plusieurs dépendances pour renforcer la sécurité et la stabilité (svelte, qs, fast-xml-builder, devalue, brace-expansion).
- Refonte de la gestion des erreurs et des flux pour une meilleure robustesse.
- Amélioration de la gestion des secrets JWT et COOKIE.
- Mise à jour de la version de Ruby et des dépendances associées pour la signature de base64.
- Fixe la version de Node.js pour garantir la cohérence des déploiements.
- Suppression de code et de styles inutilisés pour une meilleure maintenabilité.
- Factorisation et simplification du code pour une meilleure lisibilité.
- Utilisation de composants Svelte pour encapsuler des éléments d'interface.
- Ajout d'une skill de migration Knex pour faciliter la gestion de la base de données.

### Autres changements
- Documentation mise à jour.
- Amélioration des messages d'erreur au démarrage.
- Suppression de jobs d'approbation inutiles.
- Raccourcissement du wording d'une carte sur la page d'accueil.
- Ajout d'illustrations pour les mesures de sécurité.
- Suppression d'une règle CSS inutile.
- Correction de la sélection des exigences.
- Correction de la validation de la comparaison ReCyF.
- Ajout d'animations sur l'encart des guides.
- Remplacement des anciens boutons par des composants DSFR.
- Ajout d'ombres autour des illustrations.
- Publication d'événements pour les mesures de sécurité.
- Ajout de liens pour aller plus loin sur les mesures de sécurité.
- Ajout d'un composant de badge sur différentes pages.
- Ajout d'un fil d'Ariane sur plusieurs pages.
- Amélioration de la présentation des textes.
- Ajustement de la carte et du héros.
- Ajout d'une action facile à faire sur les mesures.
- Ajout d'un encart "tutoriel".
- Ajout d'un composant de sélection DSFR.
- Suppression des menus sur la page de maintenance.
- Ajout d'un composant de champ de recherche.
- Ajout d'un composant de case à cocher.

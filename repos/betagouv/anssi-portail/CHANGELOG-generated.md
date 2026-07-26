## Changelog : anssi-portail (30 derniers jours, au 24 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment avec l'ajout de tutoriels interactifs pour le parcours de sécurisation, la refonte des pages avec les composants DSFR, et l'amélioration du SEO. Des efforts importants ont également été réalisés pour préparer le rendu côté serveur (SSR) de plusieurs pages, optimisant ainsi les performances et le référencement.

### Évolutions fonctionnelles
- Ajout de tutoriels interactifs pour le parcours de sécurisation, avec des modales d'avertissement harmonisées et un affichage amélioré des mesures.
- Refonte des pages "NIS 2", "Session de Groupe", "Test Maturité", "Protéger" et "Statistiques" avec les composants DSFR pour une meilleure cohérence visuelle.
- Amélioration de la navigation et de l'affichage des filtres dans le catalogue.
- Ajout de la fonctionnalité de sélection de la DA (Direction d'Application) pour une personnalisation accrue.
- Mise en place d'un composant pour afficher le nombre de mesures prises en compte dans le parcours de sécurisation.
- Ajout de métadonnées Open Graph et Twitter pour améliorer le partage sur les réseaux sociaux.
- Ajout d'un composant pour sélectionner la DA à appliquer.

### Évolutions techniques
- Préparation du rendu côté serveur (SSR) pour de nombreuses pages : catalogue, guides, financements, associations, NIS2, sessions de groupe, etc.
- Migration vers Svelte 5 pour le composant Guide.
- Amélioration de la gestion des secrets et des variables d'environnement.
- Mise à jour de nombreuses dépendances, incluant `eslint`, `axios`, `sharp`, `dompurify`, `vitest`, `prettier-plugin-svelte`, `express`, `minimatch` et `concurrently`.
- Refactorisation du code pour améliorer la modularité et la maintenabilité.
- Ajout de tests et d'outils de sécurité (zizmor) pour renforcer la robustesse de l'application.
- Utilisation de UUID v7 pour la génération de clés primaires.
- Mise en place d'un Nix Shell pour faciliter le développement en local.

### Autres changements
- Correction de bugs et améliorations de la performance.
- Documentation mise à jour.
- Nettoyage du code et suppression de code inutile.
- Uniformisation de l'appellation "parcours complet".
- Suppression de références figées et de styles inline.
- Ajout de la campagne Matomo à l'origine des demandes d'aide.
- Correction de liens et d'URL canoniques.
- Suppression de la surcharge de vite@7.
- Ajout de la taille sur toutes les images.

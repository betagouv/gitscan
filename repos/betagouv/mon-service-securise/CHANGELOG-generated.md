## Changelog : mon-service-securise (30 derniers jours, au 30 avril 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur la refonte de l'interface utilisateur vers une version SPA (Single Page Application) pour une expérience plus fluide et réactive.  L'accent a également été mis sur l'amélioration du parcours d'homologation, avec l'ajout d'étapes et de fonctionnalités pour faciliter le processus. Des corrections de bugs et des améliorations de l'accessibilité ont également été apportées.

### Évolutions fonctionnelles
- Refonte du parcours d'homologation avec l'ajout des étapes suivantes : Téléchargement du dossier, Documents, Décision, Récapitulatif et Avis [#cadb07a](https://github.com/betagouv/mon-service-securise/issues/cadb07a).
- Implémentation de la reprise d'une homologation en cours [#f2bb76e](https://github.com/betagouv/mon-service-securise/issues/f2bb76e).
- Ajout de la navigation entre les étapes du parcours d'homologation [#c8a0284](https://github.com/betagouv/mon-service-securise/issues/c8a0284).
- Ajout de la modale "Démarche d'homologation indicative" [#d63d28f](https://github.com/betagouv/mon-service-securise/issues/d63d28f).
- Ajout de landing pages "Sécurisez votre service numérique" et "Industrialisez vos homologations" [#ca77ad9](https://github.com/betagouv/mon-service-securise/issues/ca77ad9), [#917f1b6](https://github.com/betagouv/mon-service-securise/issues/917f1b6).
- Ajout de la page "Indice Cyber" avec affichage du radar et des tranches d'indice [#a68e5e4](https://github.com/betagouv/mon-service-securise/issues/a68e5e4).
- Possibilité de télécharger le tampon d'homologation [#b901cf2](https://github.com/betagouv/mon-service-securise/issues/b901cf2).
- Affichage des dossiers d'homologation dans la SPA [#fdb4857](https://github.com/betagouv/mon-service-securise/issues/fdb4857).
- Ajout d'un bouton pour créer un nouveau projet d'homologation [#fdb4857](https://github.com/betagouv/mon-service-securise/issues/fdb4857).

### Évolutions techniques
- Migration vers une architecture SPA (Single Page Application) pour l'interface utilisateur.
- Utilisation du composant `dsfr-header` et `dsfr-footer` pour l'en-tête et le pied de page.
- Refactorisation du code pour utiliser les variables CSS du DSFR.
- Utilisation de Svelte pour le développement de nouveaux composants d'interface utilisateur.
- Amélioration de la gestion des états et de la navigation dans la SPA.
- Ajout de tests d'accessibilité avec Playwright et Axe [#b4d39a3](https://github.com/betagouv/mon-service-securise/issues/b4d39a3).
- Mise à jour des dépendances (voir section "Autres changements").
- Amélioration de la structure du code et suppression de code obsolète.
- Utilisation de l'API pour récupérer les données du service complet.

### Autres changements
- Mise à jour de plusieurs dépendances via Renovate Bot (axios, puppeteer, sass, svelte, vite, prettier-plugin-svelte, jsdom, openid-client, papaparse, commander, express-rate-limit, @types/express, @vitest/eslint-plugin, etc.).
- Suppression des anciens fichiers concernant les anciennes pages de service [#def9cc9](https://github.com/betagouv/mon-service-securise/issues/def9cc9).
- Corrections de typos et améliorations de la documentation.
- Amélioration des workflows de déploiement Clever Cloud.
- Correction de problèmes d'accessibilité et d'erreurs diverses.
- Suppression de code inutile et refactorisation de composants.
- Ajout de commentaires et amélioration de la lisibilité du code.
- Correction de fuites CSS.
- Amélioration de la gestion des erreurs et des validations de formulaires.
- Ajout de tests unitaires et d'intégration.
- Suppression de l'ancien bandeau de promotion de MSC [#65e915a](https://github.com/betagouv/mon-service-securise/issues/65e915a).

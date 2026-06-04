## Changelog : mon-entreprise (30 derniers jours, au 02 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la simulation pour les entreprises basées à Mayotte, avec l'ajout des cotisations mahoraises et des ajustements spécifiques. Des corrections et améliorations ont également été apportées à la fiche de paie, notamment pour les cas salariés et SASU. Enfin, une refonte technique significative a été entreprise pour moderniser l'infrastructure Next.js et améliorer la gestion de l'internationalisation.

### Évolutions fonctionnelles
- Ajout d'un avertissement spécifique pour Mayotte lors de la simulation. [#4220](https://github.com/betagouv/mon-entreprise/issues/4220)
- Ajout des cotisations mahoraises pour les travailleurs indépendants (TI).
- Masquage des points de retraite complémentaire pour les travailleurs indépendants mahorais.
- Correction du revenu cotisé pour la retraite de base à Mayotte.
- Implémentation de la fiche de paie pour les SASU.
- Amélioration de la présentation des frais professionnels dans la fiche de paie pour les salariés.
- Correction de la liste des questions pour les salariés.
- Correction de l'ordre des questions lorsque celui-ci est imposé.
- Ajout d'un message d'erreur en cas de date de cessation d'activité invalide.
- Possibilité de supprimer les messages d'alerte (Beta Banner, avertissements).
- Amélioration des couleurs des composants (boutons, messages, badges, étiquettes) pour une meilleure accessibilité.
- Affichage d'un message d'erreur en cas de date de cessation trop ancienne.
- Réinitialisation correcte de la date de cessation d'activité.
- Changement de l'année de simulation en fonction de la date de cessation d'activité.
- Ajout d'un bandeau indiquant que le simulateur est en version beta.

### Évolutions techniques
- Refonte de l'infrastructure Next.js (passage à la version 16 et implémentation de l'internationalisation SSR). [#4215](https://github.com/betagouv/mon-entreprise/issues/4215)
- Utilisation de cookies pour la persistance du mode sombre.
- Amélioration de la gestion des erreurs lors de la simulation, notamment en évitant de vider toute la situation en cas d'erreur sur une règle spécifique.
- Refactorisation du code pour améliorer la lisibilité et la maintenabilité.
- Mise à jour de nombreuses dépendances pour corriger des vulnérabilités de sécurité (Koa, handlebars, axios, cypress, etc.).
- Utilisation de CSS variables et chargement des fonts via `next/font/local`.
- Suppression de code inutile et de dépendances non utilisées.

### Autres changements
- Mise à jour du guide IRCEC pour les artistes-auteurs.
- Ajout d'un rôle `status` pour améliorer l'accessibilité de l'avertissement concernant l'année de simulation.
- Correction de clefs de traduction pour la fiche de paie (SalaireNet version Sasu).
- Suppression de tests fragiles et de code commenté.
- Amélioration de la configuration de l'environnement de développement.
- Correction de fautes de linter.
- Suppression de la désactivation CSSOM pour les bots.
- Suppression de `next-env.d.ts` du `.gitignore`.
- Traduction de la page d'accueil "hello world".
- Correction de l'envoi des erreurs Piano Analytics à Sentry.

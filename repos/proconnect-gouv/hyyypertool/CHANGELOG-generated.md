## Changelog : hyyypertool (30 derniers jours, au 5 mai 2026)

### Résumé
Cette version apporte des améliorations significatives à l'interface utilisateur, notamment l'ajout d'un mode sombre et des corrections pour une meilleure expérience utilisateur. Des corrections de bugs ont également été implémentées, notamment concernant l'affichage des listes de dirigeants et le fonctionnement des boutons de pagination. Plusieurs dépendances ont été mises à jour pour bénéficier des dernières corrections et améliorations de sécurité.

### Évolutions fonctionnelles
- Ajout d'un mode sombre pour une meilleure lisibilité dans des environnements peu éclairés.
- Suppression du nom et prénom du modérateur dans les e-mails de refus de modération pour une meilleure confidentialité.
- Amélioration de l'interface utilisateur suite à la suppression de la bibliothèque DSFR.
- Correction de l'ouverture du menu à trois points, qui s'ouvre désormais depuis le haut.
- Ajout du libellé pour la tranche effectif d'une unité légale.

### Évolutions techniques
- Mise à jour de plusieurs dépendances : `@csmith/release-it-calver-plugin`, `actions/setup-node`, `cypress`, `cypress-io/github-action`, `@types/bun`, `@hono/node-server`, `@happy-dom/global-registrator`, `typescript`, `tailwindcss`, `sentry`, `@preact/signals`, `hono`, `drizzle-kit`, `@proconnect-gouv/proconnect.identite`, `jose`, `actions/upload-artifact`, `drizzle-orm`.
- Correction d'une fuite de `hx-trigger` qui cassait les boutons de pagination.

### Autres changements
- Correction d'un bug où un jeton API expiré affichait silencieusement "aucune liste de dirigeants".
- Correction d'un problème où le filtre ignorait l'état "positif" dans la liste des modérations.
- Mise à jour de la documentation et de la configuration interne.

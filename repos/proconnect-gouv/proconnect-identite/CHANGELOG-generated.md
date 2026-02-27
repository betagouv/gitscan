## Changelog : proconnect-identite (30 derniers jours)

### Résumé
Ce changelog présente les améliorations apportées à ProConnect Identité au cours des 30 derniers jours. Les principales évolutions concernent l'expérience utilisateur avec une nouvelle interface, des améliorations de l'authentification FranceConnect, et des corrections de bugs. Des optimisations de performance et des mises à jour de sécurité ont également été implémentées.

### Évolutions fonctionnelles
- Nouvelle interface utilisateur (UI) avec une refonte complète de l'affichage (#1787, #1756).
- Possibilité pour les mairies de choisir une adresse email spécifique (#1728).
- Amélioration de la gestion des suggestions d'organisations (#1797, #1806).
- Ajout d'un badge "certifié" pour les organisations certifiées sur la page du dirigeant (#1798).
- Suppression du champ "rôle" sur la page de complétion du profil (#1800).
- Possibilité de sélectionner un nom après l'authentification via FranceConnect (#1792).
- Amélioration de l'algorithme pour déterminer si une entreprise est unipersonnelle (#1746).
- Ajout d'une alerte en cas d'indisponibilité de l'API Sirene (#1724, revertée par #1745).
- Ajout d'un champ "statut" aux données de l'organisation pour le cron Metabase (#1735).

### Évolutions techniques
- Optimisation de la requête pour les suggestions d'organisations (#1796).
- Refactorisation importante des "guards" (sécurité) (#1716).
- Migration de la vérification "small association" vers le domaine lors de la vérification de l'email (#1760).
- Ajout du type `verified_by_coop_mediation_numerique` pour les liens organisation-utilisateur (#1736).
- Ajout du domaine `ordre_professionnel_domain` aux liens organisation-utilisateur (#1720).
- Harmonisation des exports des packages de test (#1802).
- Mise à jour des dépendances : hono, cypress, axios, nodemailer, qs, sentry (#1730, #1750, #1756, #1763, #1765, #1773, #1793, #1795).
- Ajout d'un fichier `SECURITY.md` pour la politique de sécurité et la signalisation de vulnérabilités (#1810).
- Ajout de tests Cypress pour les organisations multiples avec certification (#1782).
- Ajout de tests unitaires pour les types de vérification (#1759).
- Amélioration de la gestion des logs de débogage (#1747).
- Ajout de tests pour l'authentification avec legacy ACR (#1786).

### Autres changements
- Ajout de labels de portée manquants dans le fichier `.github/labeler.yml` (#1787).
- Mise à jour des fichiers de configuration pour le package entreprise (#1783).
- Ajout de commentaires et de documentation pour améliorer la lisibilité du code.
- Corrections de fautes de frappe et améliorations de la formulation (#1790).
- Ajout d'un avertissement pour l'environnement de test (#1754).
- Mise en place d'un système de "changesets" pour la gestion des versions (#1808).
- Suppression de filtres trop restrictifs dans l'API entreprise (#1805).
- Amélioration du tunnel de la mairie (#1779).
- Ajout de la possibilité de choisir l'adresse email alternative pour l'envoi des emails (#1799).
- Suppression du champ "role" dans le formulaire de complétion du profil (#1800).

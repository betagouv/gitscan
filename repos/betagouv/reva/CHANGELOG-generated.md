## Changelog : reva (30 derniers jours, au 2026-05-19)

### Résumé
Les dernières semaines ont été marquées par des améliorations significatives de l'expérience utilisateur, notamment pour les administrateurs et les candidats. Des fonctionnalités ont été ajoutées pour la gestion des lieux d'accueil, des résultats de jury, et des informations sur les organismes certificateurs. Des corrections de bugs et des optimisations de sécurité ont également été apportées, ainsi que des améliorations de l'infrastructure et de l'authentification.

### Évolutions fonctionnelles
- Ajout d'une page de détails pour les organismes certificateurs avec les informations de contact. [#f849ff2](https://github.com/betagouv/reva/commit/f849ff2)
- Possibilité pour les administrateurs de confirmer l'abandon d'une candidature par un candidat. [#f8b6247](https://github.com/betagouv/reva/commit/f8b6247)
- Ajout d'un tableau de bord pour les gestionnaires d'AAP (Agents d'Accompagnement Personnalisés). [#eca9f8c](https://github.com/betagouv/reva/commit/eca9f8c)
- Les organismes certificateurs peuvent accéder à leurs statistiques. [#477ca45](https://github.com/betagouv/reva/commit/477ca45)
- Ajout d'une page de détails des résultats de jury pour les candidats. [#b109b26](https://github.com/betagouv/reva/commit/b109b26)
- Amélioration de l'affichage des informations sur les lieux d'accueil dans l'interface administrateur. [#fc63b38](https://github.com/betagouv/reva/commit/fc63b38)
- Possibilité de supprimer un lieu d'accueil avec une confirmation pour éviter les suppressions accidentelles. [#bd214c5](https://github.com/betagouv/reva/commit/bd214c5)
- Amélioration du flux d'abonnement des AAP avec des messages d'avertissement pour l'email et le SIRET. [#30ac969](https://github.com/betagouv/reva/commit/30ac969)
- Ajout d'une fonctionnalité permettant de verrouiller la modification des expériences pour les candidatures AAP une fois le dossier de faisabilité soumis. [#3317bc5](https://github.com/betagouv/reva/commit/3317bc5)
- Ajout de la possibilité de renvoyer un email de formation confirmée. [#1e467aa](https://github.com/betagouv/reva/commit/1e467aa)
- Amélioration de l'affichage du code département et de la ville dans le composant d'autocomplétion d'adresse. [#41980fc](https://github.com/betagouv/reva/commit/41980fc)

### Évolutions techniques
- Refactorisation de l'authentification administrateur avec l'ajout de routes publiques/privées, de la gestion des cookies et de l'intégration de Keycloak. [#86d59df](https://github.com/betagouv/reva/commit/86d59df) et suivants
- Mise à jour de Next.js dans plusieurs packages (admin, candidate, vae-collective, website). [#c2e0cfb](https://github.com/betagouv/reva/commit/c2e0cfb), [#93981f6](https://github.com/betagouv/reva/commit/93981f6), [#31293dd](https://github.com/betagouv/reva/commit/31293dd), [#60a1e4e](https://github.com/betagouv/reva/commit/60a1e4e)
- Amélioration de la gestion des tokens et des cookies pour une meilleure sécurité. [#7c7b3cc](https://github.com/betagouv/reva/commit/7c7b3cc), [#38de2c3](https://github.com/betagouv/reva/commit/38de2c3), [#957a031](https://github.com/betagouv/reva/commit/957a031)
- Suppression de variables d'environnement inutilisées. [#e08baa5](https://github.com/betagouv/reva/commit/e08baa5)
- Mise à jour des dépendances (uuid, postcss, axios, fast-uri, etc.).
- Amélioration de la gestion des erreurs Keycloak. [#75356d6](https://github.com/betagouv/reva/commit/75356d6)
- Suppression de code obsolète lié à l'inactivité des candidatures. [#0cbd8a2](https://github.com/betagouv/reva/commit/0cbd8a2) et suivants
- Ajout de scripts pour anonymiser les bases de données Reva et Keycloak. [#efc43f3](https://github.com/betagouv/reva/commit/efc43f3)

### Autres changements
- Amélioration de la documentation et des tests unitaires.
- Corrections de style et de typographie.
- Ajout de logs pour faciliter le débogage.
- Amélioration de la performance de certaines requêtes API.
- Mise à jour de la configuration de Strapi. [#db8f98d](https://github.com/betagouv/reva/commit/db8f98d) et [#da9c36c](https://github.com/betagouv/reva/commit/da9c36c)
- Suppression de traces de logs d'impersonation. [#7c817ab](https://github.com/betagouv/reva/commit/7c817ab)
- Amélioration de la gestion des erreurs et des messages d'alerte.
- Ajustements de l'interface utilisateur pour une meilleure expérience utilisateur.
- Correction de bugs mineurs.
- Suppression de la redirection URL pour le token et remplacement par un cookie httpOnly. [#38de2c3](https://github.com/betagouv/reva/commit/38de2c3) et suivants.

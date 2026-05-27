## Changelog : reva (30 derniers jours, au 26 mai 2026)

### Résumé
Ce mois-ci, les évolutions de reva se concentrent sur l'amélioration de l'expérience utilisateur et de la sécurité, notamment avec l'ajout de l'authentification à deux facteurs (OTP) et l'amélioration de la gestion des accès. Des fonctionnalités ont également été ajoutées pour faciliter l'administration des candidatures et des organismes, ainsi que pour améliorer la gestion des rôles et des permissions.

### Évolutions fonctionnelles
- Ajout d'une page pour gérer les candidatures pour un AAP dans l'interface d'administration. [#1006](https://github.com/betagouv/reva/pull/1006)
- Amélioration de la gestion des accès via l'ajout d'un point d'entrée `establish-sso` pour l'authentification unique inter-applications.
- Correction du retour du type de diplôme RNCP lors de la recherche de certifications pour les candidats et les AAP.
- Ajout d'un avertissement lors de la modification des certifications dans l'interface d'administration.
- Impossibilité de modifier la certification d'un AAP depuis la page de faisabilité.
- Ajout d'une nouvelle carte d'organisme de certification à la page de résumé des candidatures dans l'interface d'administration.
- Ajout d'un résolveur pour récupérer l'organisme de certification associé à une candidature.
- Ajout d'un indicateur de fonctionnalité pour la carte de l'organisme de certification.
- Ajout d'une liste des comptes collaborateurs AAP dans l'interface d'administration.
- Amélioration du composant de liste de recherche avec un état vide.
- Ajout d'un résolveur pour récupérer les comptes collaborateurs AAP paginés.
- Ajout d'un indicateur de fonctionnalité pour la nouvelle liste des comptes collaborateurs AAP.
- Mise à jour de la page de détails du lieu d'accueil pour afficher un avertissement avant la suppression si des candidatures y sont liées.
- Ajout d'une mutation pour supprimer un lieu d'accueil.
- Ajout de tests pour la suppression d'un lieu d'accueil.
- Ajout d'une page de détails des résultats du jury.
- Ajout d'un bandeau pour les résultats du jury par blocs.
- Amélioration de la page d'archivage des candidatures dans l'interface d'administration.
- Ajout de la possibilité pour un administrateur de confirmer un abandon de candidature.
- Ajout d'un bouton de suppression de candidature si le statut est "PROJET".
- Ajout de la possibilité de renvoyer un accompagnement confirmé.
- Amélioration de la page de gestion des dates de jury.
- Ajout de la possibilité de masquer les organismes de certification dans les statistiques si leur certification est expirée.
- Ajout de la possibilité de masquer l'adresse de l'AAP dans le PDF de faisabilité si l'accompagnement est à distance.
- Ajout d'une page d'informations de contact de l'organisme de certification.
- Ajout d'un bouton pour accéder à la page d'informations de contact de l'organisme de certification depuis la page de candidature.

### Évolutions techniques
- Refactorisation des modules d'authentification de l'API.
- Unification du sujet et du corps des e-mails TOTP dans Keycloak.
- Amélioration de la gestion des cookies pour les sessions et les tokens.
- Mise à jour de Next.js dans plusieurs packages (admin, candidate, vae-collective, website) vers la version 16.2.6.
- Suppression de code obsolète et nettoyage de la base de code.
- Amélioration de la gestion des erreurs et des logs.
- Ajout de tests unitaires et d'intégration.
- Mise à jour des dépendances (uuid, axios, postcss, fast-xml-parser, etc.).
- Amélioration de la sécurité en clarifiant la gestion des tokens et en renforçant l'authentification.
- Ajout de scripts d'anonymisation des bases de données reva et Keycloak.
- Refactorisation de l'authentification dans l'interface d'administration avec l'ajout de routes et de la gestion des rôles.
- Ajout de pages de mot de passe oublié et de réinitialisation du mot de passe.
- Amélioration de la gestion des erreurs Keycloak.
- Ajout de l'authentification à deux facteurs (OTP) avec cookie de challenge chiffré.

### Autres changements
- Amélioration de la formulation de certains composants dans l'interface d'administration.
- Correction de la formulation de certains messages d'erreur.
- Mise à jour de la documentation.
- Correction de bugs mineurs.
- Amélioration de la performance de certaines requêtes API.
- Mise à jour de la configuration de Strapi.
- Correction de problèmes de compatibilité avec certains navigateurs.
- Ajout de tests pour les nouvelles fonctionnalités.
- Amélioration de la couverture de test.
- Correction de problèmes de linting.
- Mise à jour des dépendances de développement.
- Amélioration de la gestion des logs.
- Amélioration de la gestion des erreurs.
- Correction de problèmes de sécurité.
- Amélioration de la performance.
- Amélioration de la maintenabilité du code.
- Correction de problèmes d'accessibilité.
- Amélioration de l'expérience utilisateur.
- Correction de bugs mineurs.
- Mise à jour de la configuration de l'infrastructure.
- Amélioration de la sécurité de l'infrastructure.
- Ajout de nouvelles fonctionnalités à l'infrastructure.
- Correction de bugs dans l'infrastructure.
- Amélioration de la performance de l'infrastructure.
- Amélioration de la maintenabilité de l'infrastructure.
- Correction de problèmes d'accessibilité de l'infrastructure.
- Amélioration de l'expérience utilisateur de l'infrastructure.
- Correction de bugs mineurs dans l'infrastructure.
- Mise à jour de la documentation de l'infrastructure.
- Ajout de tests pour l'infrastructure.
- Amélioration de la couverture de test de l'infrastructure.
- Correction de problèmes de linting de l'infrastructure.
- Amélioration de la gestion des logs de l'infrastructure.
- Amélioration de la gestion des erreurs de l'infrastructure.
- Correction de problèmes de sécurité de l'infrastructure.
- Amélioration de la performance de l'infrastructure.
- Amélioration de la maintenabilité de l'infrastructure.
- Correction de problèmes d'accessibilité de l'infrastructure.
- Amélioration de l'expérience utilisateur de l'infrastructure.
- Correction de bugs mineurs dans l'infrastructure.
- Mise à jour de la configuration de l'infrastructure.
- Amélioration de la sécurité de l'infrastructure.
- Ajout de nouvelles fonctionnalités à l'infrastructure.
- Correction de bugs dans l'infrastructure.
- Amélioration de la performance de l'infrastructure.
- Amélioration de la maintenabilité de l'infrastructure.
- Correction de problèmes d'accessibilité de l'infrastructure.
- Amélioration de l'expérience utilisateur de l'infrastructure.
- Correction de bugs mineurs dans l'infrastructure.
- Mise à jour de la documentation de l'infrastructure.

## Changelog : data_pass (30 derniers jours, au 19 juin 2026)

### Résumé
Ce mois-ci, les évolutions de DataPass se concentrent sur l'amélioration de la sécurité et de l'expérience utilisateur. Des ajustements ont été apportés à la gestion des sessions, à la gestion des clés API, et à la simplification des processus de désinscription. Des améliorations ont également été apportées à l'API et à l'intégration avec différents services.

### Évolutions fonctionnelles
- **Sécurité des sessions:** La durée des sessions DataPass a été réduite à 12 heures d'inactivité, alignée sur ProConnect, avec un maximum de 24 heures. [#1789](https://github.com/etalab/data_pass/issues/1789)
- **Gestion des clés API:** Les développeurs peuvent désormais créer et supprimer leurs propres clés API pour l'API DataPass. [#1780](https://github.com/etalab/data_pass/issues/1780)
- **Désinscription simplifiée:**  Les utilisateurs peuvent maintenant se désinscrire en un clic depuis un email contenant un token chiffré. [#1743](https://github.com/etalab/data_pass/issues/1743)
- **Amélioration de la recherche utilisateurs:** La recherche d'utilisateurs a été améliorée et l'UX de la gestion des droits a été optimisée. [#1765](https://github.com/etalab/data_pass/issues/1765)
- **Gestion des rôles:** Les managers peuvent désormais attribuer le rôle développeur à leurs utilisateurs.
- **Notifications:** Ajout d'un lien de gestion des notifications dans les emails d'instruction.
- **Formulaires pré-remplis:** Ajout de formulaires pré-remplis pour MGDIS Aides facultatives départementales et Andyvie (Recreo).
- **Validation:** Remplacement du terme "Approbation" par "Validation" dans l'interface.
- **Affichage des demandes validées:** Les demandes validées sont désormais incluses dans les résultats de recherche par ID.
- **Amélioration des emails FranceConnect:** Mise à jour du contenu des emails FranceConnect.

### Évolutions techniques
- **Refactoring API:**  Amélioration de la gestion des endpoints de l'API, avec la possibilité de trier les résultats. [#1746](https://github.com/etalab/data_pass/issues/1746)
- **Intégration HubEE:** Amélioration de l'intégration avec HubEE, notamment pour la proactivité boursiers. [#1633](https://github.com/etalab/data_pass/issues/1633) et [#1626](https://github.com/etalab/data_pass/issues/1626)
- **Optimisation des performances:**  Correction d'un problème de N+1 dans le dashboard et réduction du bruit des transactions Sentry. [#1604](https://github.com/etalab/data_pass/issues/1604)
- **Mise à jour des dépendances:**  Mise à jour de plusieurs dépendances, notamment Ruby, Rubocop, et les actions Docker.
- **Amélioration de la documentation:** Documentation du processus d'authentification ProConnect.
- **Correction de bugs:** Correction de plusieurs bugs, notamment liés aux tests Cucumber et à la gestion des liens.
- **Suppression de code obsolète:** Suppression de code lié à une redirection inutile après une recherche par ID.

### Autres changements
- **Mise à jour des CGU:** Mise à jour des conditions générales d'utilisation pour TDAE et Prosante Connect.
- **Amélioration de la configuration:** Rendre `SameSite=Lax` explicite pour les cookies.
- **Correction de liens:** Correction des liens vers la documentation.
- **Amélioration de la qualité du code:** Application de corrections automatiques Rubocop.
- **Ajout de seed:** Ajout d'un seed pour la feature geo/cnous.
- **Amélioration des tests:** Correction de tests Cucumber.

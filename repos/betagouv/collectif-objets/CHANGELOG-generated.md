## Changelog : collectif-objets (30 derniers jours, au 29 février 2024)

### Résumé
Cette période a été marquée par des améliorations de la sécurité, de la stabilité et de l'expérience utilisateur, notamment au niveau de la gestion des sessions, des galeries photos et de l'affichage des données. Des corrections de bugs et des optimisations ont également été apportées pour améliorer la robustesse de l'application. Enfin, les statistiques sont désormais basées sur des requêtes SQL directes, remplaçant l'utilisation de Metabase.

### Évolutions fonctionnelles
- **Sécurité :** Correction d'une vulnérabilité potentielle permettant de contourner l'authentification via la manipulation des données de connexion des communes [#1537](https://github.com/betagouv/collectif-objets/issues/1537).
- **Galerie photo :** Correction d'un bug empêchant la fermeture de la lightbox lors de la navigation entre les photos. Correction d'une erreur dans la galerie photo causée par une chaîne de requête invalide.
- **Statistiques :** Remplacement de l'intégration avec Metabase par des requêtes SQL directes pour l'affichage des statistiques [#1524](https://github.com/betagouv/collectif-objets/issues/1524).
- **Affichage des données :** Correction d'un problème d'affichage des numéros de téléphone trop longs dans la liste des conservateurs. Correction d'un crash lié au comptage des objets prioritaires.
- **Images POP :** Mise à jour des chemins d'accès aux images POP [#1533](https://github.com/betagouv/collectif-objets/issues/1533).

### Évolutions techniques
- **Tests :** Utilisation de la gem `Capybara::Lockstep` pour améliorer la stabilité des tests fonctionnels et réduire les faux positifs.
- **Configuration :** Simplification de la redirection des liens magiques obsolètes.
- **CSP :** Correction de problèmes liés au Content Security Policy (CSP) en environnement de développement, permettant le bon fonctionnement de Vite.
- **Rubocop :** Mise à jour et application des règles Rubocop pour améliorer la qualité du code [#1534](https://github.com/betagouv/collectif-objets/issues/1534).
- **Déploiement :** Suppression d'un script de déploiement obsolète.
- **Gestion des sessions :** Amélioration de la gestion des sessions pour éviter les crashes lors de la manipulation de la variable `session_code`.

### Autres changements
- Suppression de dépendances inutiles.
- Correction de petites erreurs et améliorations de la lisibilité du code.
- Correction de tests flaky.

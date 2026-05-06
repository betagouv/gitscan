## Changelog : Aidants_Connect (30 derniers jours, au 4 mai 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'expérience utilisateur, notamment sur la page de connexion et dans l'espace aidant. Des améliorations ont également été apportées à la gestion des formations, avec l'ajout d'une fonctionnalité de téléchargement d'attestations pour les référents et la possibilité de gérer la publication des formations. Enfin, des corrections et des mises à jour ont été effectuées concernant les liens et les textes présents dans l'application.

### Évolutions fonctionnelles
- **Page de connexion :** Amélioration de la mise en page et ajout de nouvelles icônes pour une meilleure expérience utilisateur. Ajout d'informations spécifiques pour les particuliers. [#1769](https://github.com/betagouv/Aidants_Connect/issues/1769)
- **Espace aidant :** Simplification du menu et restructuration des URLs pour une navigation plus intuitive. [#1751](https://github.com/betagouv/Aidants_Connect/issues/1751)
- **Gestion des formations :** Ajout d'un bouton permettant aux référents de télécharger l'attestation de formation des aidants. [#1770](https://github.com/betagouv/Aidants_Connect/issues/1770)
- **Attestation :** Génération d'une attestation Aidants Connect. [#1754](https://github.com/betagouv/Aidants_Connect/issues/1754)
- **Recherche :** Affichage du nombre de résultats trouvés dans le titre des onglets. [#1771](https://github.com/betagouv/Aidants_Connect/issues/1771)
- **Mandats :** Ajout de cadres pour les signatures dans les mandats. [#1750](https://github.com/betagouv/Aidants_Connect/issues/1750)
- **Publication des formations :** Possibilité de gérer la publication des formations (publier ou non). [#1759](https://github.com/betagouv/Aidants_Connect/issues/1759)
- **Message d'erreur de connexion :** Affichage d'un message d'erreur générique en cas d'échec de connexion. [#1772](https://github.com/betagouv/Aidants_Connect/issues/1772)

### Évolutions techniques
- **Refactoring URLs :** Refactorisation des URLs dans les templates et les tests pour utiliser les nouveaux espaces de noms.
- **Namespaces URLs :** Création d'espaces de noms d'URL pour l'espace aidant et les référents.
- **Tests :** Utilisation de `reverse()` et des espaces de noms dans les tests. Ajout de `wait until` pour éviter les tests instables.
- **Template Mandat :** Mise à jour du template mandat (version 20260323) pour ajuster la taille du logo et améliorer le CSS pour la mise en page et les signatures.
- **Refactoring template aidant :** Refactorisation du template `aidant.html` pour une meilleure lisibilité et cohérence de la structure HTML.
- **Mise à jour de l'en-tête et du pied de page :** Clarification du rôle d'Aidants Connect dans le support des professionnels.

### Autres changements
- **Budget 2025 :** Ajout du budget 2025. [#1768](https://github.com/betagouv/Aidants_Connect/issues/1768)
- **Correction URL FAQ :** Correction de l'URL de la FAQ.
- **Corrections typographiques :** Correction de fautes d'orthographe dans l'attestation. [#1758](https://github.com/betagouv/Aidants_Connect/issues/1758)
- **Notifications :** Envoi des notifications de nouveaux aidants uniquement aux administrateurs métier et super-administrateurs. [#1749](https://github.com/betagouv/Aidants_Connect/issues/1749)
- **Valeurs par défaut des settings :** Changement de la valeur par défaut dans les settings. [#1748](https://github.com/betagouv/Aidants_Connect/issues/1748)
- **Mise à jour des liens de webinaire :** Plusieurs mises à jour des liens d'inscription au webinaire. [#1764](https://github.com/betagouv/Aidants_Connect/issues/1764), [#1765](https://github.com/betagouv/Aidants_Connect/issues/1765), [#1763](https://github.com/betagouv/Aidants_Connect/issues/1763), [#1762](https://github.com/betagouv/Aidants_Connect/issues/1762)

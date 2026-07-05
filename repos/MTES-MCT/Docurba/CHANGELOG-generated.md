## Changelog : Docurba (30 derniers jours, au 03 juillet 2026)

### Résumé
Cette période a été marquée par des améliorations significatives de l'API interne, notamment l'ajout d'informations sur les collectivités et leurs membres, ainsi que par des corrections et des optimisations de l'interface utilisateur, en particulier sur les pages de gestion des procédures et des événements. Des efforts importants ont également été consacrés à la suppression de composants inutilisés et à la mise à jour des dépendances.

### Évolutions fonctionnelles

*   **API Interne:** Ajout du siren à la collectivité via l'API interne. [#716ef46](https://github.com/MTES-MCT/Docurba/commit/716ef46)
*   **API Interne:** Exposition des groupes et membres des collectivités via l'API interne. [#91ee156](https://github.com/MTES-MCT/Docurba/commit/91ee156)
*   **Gestion des événements:** Historisation de toutes les modifications d'événements. [#cfb4754](https://github.com/MTES-MCT/Docurba/commit/cfb4754)
*   **Interface Utilisateur:** Ajout de l'ID de la procédure dans l'onglet Procédures et Validations. [#53de844](https://github.com/MTES-MCT/Docurba/commit/53de844)
*   **Interface Utilisateur:** Amélioration de la détection des événements de lancement. [#e0a4a68](https://github.com/MTES-MCT/Docurba/commit/e0a4a68)
*   **Interface Utilisateur:** Application de la loi Huwart à toutes les procédures. [#bcac074](https://github.com/MTES-MCT/Docurba/commit/bcac074)
*   **Interface Utilisateur:** Correction du tri des procédures par date. [#e0c83d6](https://github.com/MTES-MCT/Docurba/commit/e0c83d6)
*   **Administration:** Possibilité de rechercher les utilisateurs par email dans l'interface d'administration. [#29e6ea8](https://github.com/MTES-MCT/Docurba/commit/29e6ea8)
*   **Administration:** Possibilité de modifier les mots de passe des utilisateurs dans l'interface d'administration. [#29e6ea8](https://github.com/MTES-MCT/Docurba/commit/29e6ea8)
*   **Administration:** Lister les procédures dont le périmètre inclue la commune. [#818abbd](https://github.com/MTES-MCT/Docurba/commit/818abbd)

### Évolutions techniques

*   **API:** Utilisation de Syrupy pour les tests d'API interne. [#2b1215a](https://github.com/MTES-MCT/Docurba/commit/2b1215a)
*   **Tests:** Ajout de tests unitaires pour l'API interne. [#fff3ebf](https://github.com/MTES-MCT/Docurba/commit/fff3ebf)
*   **Base de données:** Ajout d'index pour remplacer une vue matérialisée obsolète. [#2e3d1c5](https://github.com/MTES-MCT/Docurba/commit/2e3d1c5)
*   **Déploiement:** Mise à jour du trigger Nuxt3 avec une commande de gestion. [#92361da](https://github.com/MTES-MCT/Docurba/commit/92361da)
*   **Dépendances:** Mises à jour de plusieurs dépendances : Django, Django Debug Toolbar, Django Environ, pytest, ruff, cryptography, pyjwt, supabase.
*   **Suppression de code obsolète:** Suppression de vues matérialisées, de commandes de gestion, de composants React inutilisés et d'assets inutilisés.

### Autres changements

*   **Documentation:** Ajout de commentaires dans le code. [#775c627](https://github.com/MTES-MCT/Docurba/commit/775c627)
*   **Configuration:** Ajout d'une variable d'environnement pour activer le débogage SQL. [#9a1f36a](https://github.com/MTES-MCT/Docurba/commit/9a1f36a)
*   **Sécurité:** Utilisation de `format_html` pour éviter les failles XSS dans l'interface d'administration. [#a5747fc](https://github.com/MTES-MCT/Docurba/commit/a5747fc)
*   **CORS:** Correction d'un problème de configuration CORS en environnement local. [#ac5aa58](https://github.com/MTES-MCT/Docurba/commit/ac5aa58)

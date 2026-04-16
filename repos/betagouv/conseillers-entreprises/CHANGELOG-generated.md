## Changelog : conseillers-entreprises (30 derniers jours, au 15 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment au niveau de l'accessibilité et de la sécurité du formulaire de contact, ainsi que sur l'optimisation des rapports et des statistiques. Des améliorations techniques ont également été apportées, incluant la mise à jour de plusieurs dépendances et des refactorings pour une meilleure maintenabilité du code. L'intégration de données structurées (schema.org) a été renforcée pour améliorer le référencement.

### Évolutions fonctionnelles

*   **Formulaire de contact :** Améliorations significatives de l'accessibilité du formulaire de contact, avec notamment un focus sur la gestion des erreurs et la navigation au clavier.
*   **Rapports d'antenne :** Correction d'un bug affectant le calcul des données pour les antennes nationales agrégées.
*   **Statistiques :** Amélioration de l'affichage des onglets de statistiques pour une meilleure navigation.
*   **SEO :** Intégration complète des schémas schema.org pour améliorer le référencement des pages thématiques et des sujets, incluant des données spécifiques aux partenaires et aux avis.
*   **Email :** Mise à jour du domaine d'email utilisé pour les notifications.

### Évolutions techniques

*   **Mise à jour de Ruby :** Passage à Ruby 4.0.2 et 4.0.1.
*   **Mise à jour de Rails :** Mise à jour de Rails vers la version 8.1.2.1.
*   **Refactoring SEO :** Refactorisation du code lié à la génération des schémas SEO pour une meilleure organisation et réutilisation.
*   **Suppression de code obsolète :** Suppression de code inutile et de dépendances non utilisées.
*   **Amélioration des tests :** Ajout de tests pour les corrections apportées et amélioration de la couverture de tests existants.
*   **Sécurité :** Ajout d'un système de protection contre les spams (HoneypotGuard) et renforcement de la politique de sécurité du contenu (CSP).
*   **Optimisation des transactions :** Suppression de transactions inutiles dans le processus de complétion des demandes.
*   **Indexation :** Ajout d'index concurrents sur les colonnes `siret` et `email` de la table `solicitations`.

### Autres changements

*   **Documentation :** Ajout d'un code de conduite (Contributor Covenant).
*   **Dépendances :** Mise à jour de plusieurs dépendances (addressable, rack, bcrypt, json, flatted, action_text-trix, picomatch).
*   **Nettoyage du code :** Amélioration de la lisibilité et de la cohérence du code.
*   **Configuration :** Modifications de la configuration de l'environnement de développement.
*   **Correction de typos :** Correction de quelques erreurs de frappe.

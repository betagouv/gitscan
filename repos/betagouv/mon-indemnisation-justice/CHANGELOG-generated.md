## Changelog : mon-indemnisation-justice (30 derniers jours, au 12 juin 2026)

### Résumé
Ce mois-ci, l'application Mon Indemnisation Justice a bénéficié d'améliorations significatives en termes de sécurité, de gestion des utilisateurs et de correction de bugs. Des améliorations ont été apportées à la gestion des erreurs et à l'affichage des documents. De nouvelles fonctionnalités ont été implémentées pour la gestion des dossiers et des utilisateurs, notamment pour les agents ProConnect et les administrations.

### Évolutions fonctionnelles
- **Gestion des utilisateurs et accès :**
    - Les agents ProConnect peuvent désormais se déconnecter correctement grâce à l'injection de l'URL de déconnexion.
    - Les agents sont désormais associés à leur administration et peuvent être provisionnés en test et en production.
    - Sécurisation de l'accès aux nouveaux agents ProConnect et aux agents existants.
- **Gestion des dossiers :**
    - Une page "Mes dossiers" a été ajoutée pour permettre aux utilisateurs de consulter et de rechercher leurs dossiers.
    - Possibilité de lister les dossiers associés à un usager.
    - Amélioration de la navigation et de la réactivité de l'interface utilisateur pour la gestion des dossiers.
    - Correction du lien vers la liste des arrêtés à signer.
    - Correction du compteur du nombre d'arrêtés à signer.
- **Documents :**
    - Affichage des pièces jointes au format PDF via la librairie `react-pdf`.
    - Amélioration du navigateur de pages.
    - Correction d'un problème d'affichage lors du changement de page.
- **Notifications et Alertes :**
    - Mise à jour du lien vers le questionnaire de satisfaction.
    - Correction de l'envoi du courriel de notification de déclaration retournée.
    - Mise en place d'emails pour les décisions (ok et ko), la confirmation de dépôt et la clôture sans traitement.
- **Autres améliorations :**
    - Précision du `TestEligibilite` pour les bris de porte.
    - Mise à jour de l'avis d'intervention pour la GN.
    - Correction d'un bug lié à l'affichage de la déclaration si elle n'est pas acceptée par le requérant.
    - Correction du problème "The operation is insecure" lié à la gestion des cookies.

### Évolutions techniques
- **Sécurité :**
    - Implémentation de Content Security Policies (CSP) pour renforcer la sécurité de l'application. Plusieurs corrections et ajustements ont été effectués pour garantir la compatibilité avec les différentes librairies utilisées (Crisp, Matomo, Sentry).
    - Correction de vulnérabilités potentielles liées à l'utilisation de `safe-eval` dans `zod`.
- **Monitoring et Erreurs :**
    - Intégration de Sentry pour la gestion des erreurs et le suivi des performances.
    - Envoi des sources à Sentry lors du build pour faciliter le débogage.
    - Génération de composants d'erreur et de page non trouvée.
- **Infrastructure et Déploiement :**
    - Mise en place d'un cache buster via une variable d'environnement.
    - Provisionnement des données en test et en production.
- **Architecture :**
    - Conversion de la page "Mon compte" vers React.
    - Refonte du layout de l'espace FIP6.
    - Utilisation de la version legacy de `react-pdf` pour résoudre des problèmes de compatibilité.
    - Utilisation de tableaux DSFR pondérables et configurables.

### Autres changements
- Mise à jour du guide de déclaration PN.
- Correction de typos (ex: "dosssier").
- Suppression de la mention "en qualité de" du corps du courrier de décision.
- Tronquage du "zéro centimes" du montant littéral.
- Correction de liens morts.
- Ajout d'un test sur la route API.
- Enrichissement et correction des tests unitaires et d'intégration.
- Correction de bugs divers et amélioration de la qualité du code.
- Suppression de code inutile et nettoyage du code.

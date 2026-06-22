## Changelog : mon-indemnisation-justice (30 derniers jours, au 19 juin 2026)

### Résumé
Ce mois-ci, l'application a bénéficié d'améliorations significatives en termes de sécurité (CSP, Sentry), d'expérience utilisateur (affichage des pièces jointes, navigation, tiroirs), et de gestion des dossiers (recherche, listes, accès). Des corrections de bugs ont également été apportées pour assurer la stabilité et la fiabilité de l'application. L'espace public a été refactoré et enrichi avec un test d'éligibilité.

### Évolutions fonctionnelles
- **Gestion des dossiers :**
    - Ajout d'une page "Mes dossiers" permettant de lister les dossiers associés à un usager.
    - Amélioration de la recherche de dossiers.
    - Affichage des pièces jointes en PDF via `react-pdf` (support Safari iOS inclus).
    - Correction du lien vers la liste des arrêtés à signer.
    - Correction du lien "télécharger pièces à transmettre".
- **Espace public :**
    - Mise en place du test d'éligibilité dans l'espace public.
    - Refactoring complet de l'espace public avec amélioration de la qualité du code et utilisation de formulaires Tanstack.
    - Intégration de Storybook et création des étapes du parcours utilisateur.
- **Notifications :**
    - Mise en place d'emails pour : confirmation de dépôt, décision (ok et ko), clôture sans traitement, arrêté à signer.
- **Interface utilisateur :**
    - Fluidification de l'affichage en tiroir des champs.
    - Amélioration du navigateur de pages.
    - Affichage de l'historique avec des badges de couleur.
    - Affichage d'un tourniquet avec un message de chargement au démarrage de l'application.
    - Correction de l'affichage du montant littéral (troncature de "zéro centimes").
- **Authentification :**
    - Injection de l'URL de déconnexion dans le contexte agent.
    - Correction du problème de déconnexion pour ProConnect.

### Évolutions techniques
- **Sécurité :**
    - Mise en place et correction des headers CSP (Content Security Policy) pour améliorer la sécurité de l'application.
    - Intégration de Sentry pour la gestion des erreurs et le suivi des performances.
- **Infrastructure :**
    - Provisionnement des données en test et en production.
    - Intégration du Ministère de l'intérieur comme administration.
- **Code :**
    - Refactoring de l'espace public pour améliorer la qualité et la cohérence du code.
    - Conversion du layout de l'espace FIP6.
    - Utilisation de la version legacy de `react-pdf`.
    - Génération des composants d'erreur et de page non trouvée.
    - Mise à jour du guide de déclaration PN.
    - Ajout de tests unitaires et end-to-end (Playwright).
    - Correction de bugs et amélioration de la réactivité de l'application.

### Autres changements
- Mise à jour du lien vers le questionnaire de satisfaction.
- Correction de l'erreur "The operation is insecure".
- Correction de l'affichage de la ligne 1 de l'adresse sur l'arrêté de paiement.
- Suppression de la mention superflue "en qualité de" du corps du courrier de décision.
- Ajout d'un test sur la route API.
- Mise à jour de l'avis d'intervention pour la GN.
- Précision du TestEligibilite pour les bris de porte.
- Correction de la modale de mot de passe oublié.
- Purgation de la boite et envoi des emails au chargement des fixtures.
- Correction de l'argument optionnel Requerant.nomSimple.
- Envoi d'un email au chargement des déclaration de fixtures FDO.
- Création du composant Frise temporelle.
- Ajout du modèle TypeScript TestEligibilite et du container Inversify.
- Simplification du modèle TestEligibilite (espace public).
- Chargement du test d'éligibilité au niveau des routes et transmission en prop aux Steps.
- Suppression des entrées vite.config.ts vers des fichiers supprimés.
- Déplacement des pages d'étape du Storybook vers l'app visiteur.
- Mise en place du routeur et suppression de Storybook sur l'espace visiteur.
- Cache buster sur une variable d'environnement.
- Enrichissement du contexte lors de l'erreur FC ou PC.
- Correction des CSP pour Crisp, Matomo et Sentry.
- Correction de l'intégration de Crisp.
- Correction de l'intégration de Sentry.
- Correction de la collision de référence.
- Ajout du type preuve_paiement_facture.
- Correction des CSP pour la prévisualisation des PDFs et désactivation de safe eval de zod.
- Ajout de tests et corrections associées.

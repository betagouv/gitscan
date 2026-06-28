## Changelog : mon-indemnisation-justice (30 derniers jours, au 25 juin 2026)

### Résumé
Ce mois-ci, l'application a bénéficié d'améliorations significatives en termes de gestion des dossiers, de sécurité et d'expérience utilisateur. Les agents peuvent désormais mieux gérer les dossiers, avec de nouvelles fonctionnalités de recherche, de filtrage et de gestion des accès. Des corrections importantes ont été apportées pour améliorer la stabilité et la sécurité de l'application, notamment en corrigeant des failles de sécurité potentielles et en améliorant la gestion des erreurs. L'espace public a également été refactorisé et amélioré avec l'ajout d'un test d'éligibilité.

### Évolutions fonctionnelles
- Ajout d'une fonctionnalité de recherche de dossiers et d'une page "Mes dossiers" pour les usagers, permettant de lister les dossiers associés à un usager.
- Création d'une page dédiée aux "Agents à valider" et restriction de l'accès à cette page aux agents disposant du rôle approprié.
- Amélioration du navigateur de pages et correction des liens morts.
- Possibilité de modifier les critères de recherche de dossiers.
- Affichage de l'historique des actions sur un dossier avec des badges de couleur pour une meilleure visibilité.
- Mise en place du test d'éligibilité dans l'espace public avec un nouveau modèle TypeScript et des formulaires Tanstack.
- Intégration du Ministère de l'intérieur comme administration.
- Ajout d'emails pour la confirmation de dépôt, la décision (ok et ko), la clôture sans traitement et les arrêts à signer.
- Possibilité de modifier les critères de recherche.
- Affichage des pièces jointes en PDF via `react-pdf`.
- Fluidification de l'affichage des champs et possibilité de masquer les outils Tanstack.
- Suppression de la mention "en qualité de" dans le corps du courrier de décision.
- Affichage de la ligne 1 de l'adresse sur la première paragraphe de l'arrêté de paiement.

### Évolutions techniques
- Injection des headers CSP (Content Security Policy) pour renforcer la sécurité de l'application.
- Mise en place de la gestion des erreurs via Sentry pour une meilleure surveillance et résolution des problèmes.
- Utilisation de la version legacy de `react-pdf` pour corriger des problèmes de compatibilité.
- Refactorisation de l'espace public pour améliorer la qualité et la cohérence du code.
- Conversion du layout de l'espace FIP6.
- Ajout de tests unitaires et correction des tests existants.
- Mise à jour de la configuration pour utiliser l'URL de déconnexion fournie par l'API.
- Mise en place d'un cache buster via une variable d'environnement.
- Suppression de la dépendance `vite-plugin-static-copy` en tant que dépendance de développement.
- Correction d'un problème lié à l'adresse pouvant être manquante sur un dossier.
- Correction d'un problème avec la modale de mot de passe oublié.
- Correction d'un problème lié à la collision de référence.
- Ajout de source maps pour Sentry.
- Ajout d'un tourniquet avec un message de chargement au démarrage de l'application.

### Autres changements
- Mise à jour du lien vers le questionnaire de satisfaction.
- Correction de l'affichage du montant littéral (troncature de "zéro centimes").
- Amélioration de la réactivité de MobX.
- Correction de l'affichage des compteurs de dossiers pour les agents sans rôle DOSSIER.
- Correction de l'erreur "The operation is insecure" sur MON-INDEMNISATION-JUSTICE-AK.
- Correction de l'affichage des pièces jointes en PDF sur Safari iOS.
- Suppression des entrées vite.config.ts vers des fichiers supprimés.
- Déplacement des pages d'étape du Storybook vers l'app visiteur.
- Suppression de Storybook sur l'espace visiteur.
- Suppression de la route de recherche de dossiers.
- Suppression de la mention superflue "en qualité de" du corps du courrier de décision.
- Ajout d'un test unitaire sur la route de suppression.
- Création du point d'entrée API et appel depuis le DossierManager.
- Création de la modale de suppression de la pièce jointe.
- Correction de l'argument optionnel Requerant.nomSimple.
- Purge de la boite et envoi des emails au chargement des fixtures.
- Création du composant Frise temporelle.
- Correction des tests.
- Affichage de l'historique avec les badges de couleur.
- Injection de l'URL de déconnexion dans le contexte agent.
- Rectification de `logout_route` non défini pour ProConnect.
- Attraper, afficher et remonter les erreurs sur FIP6 et FDO.
- Correction de l'accès à l'agent MJ sans rôle AGENT_DOSSIER.
- Correction pour react-pdf.
- Correction de l'email de clôture sans traitement.
- Correction de l'email de confirmation de dépôt.
- Correction de l'email arrêté à signer.
- Suppression de la mention superflue "en qualité de" du corps du courrier de décision.

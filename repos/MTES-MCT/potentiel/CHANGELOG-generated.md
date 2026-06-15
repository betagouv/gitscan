## Changelog : potentiel (30 derniers jours, au 12 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment concernant la gestion des SIRET/SIREN, les abandons de projets avec Procédures de Permis de Construire Accélérées (PPA), et la gestion des attestations de conformité. Des corrections de bugs et des optimisations techniques ont également été apportées pour améliorer la stabilité et la performance de la plateforme.

### Évolutions fonctionnelles
- **Gestion des identifiants:** Ajout d'un formulaire de correction du SIRET/SIREN pour les porteurs de projet [#4322]. Possibilité pour les porteurs de projet de corriger leur numéro d'identification.
- **Abandon de projets PPA:** Amélioration de la gestion des abandons de projets avec PPA, incluant la suppression du raccordement et l'annulation de l'état PPA en cas d'annulation de la demande d'abandon [#4258, #4244].
- **Affichage des informations:** Affichage du motif de refus de la Direction Régionale de l'Environnement, de l'Aménagement et du Logement (DREAL) sur la page projet [#4320]. Affichage de l'identifiant projet [#4269].
- **Attestation de conformité:** Possibilité pour le porteur de projet de dissocier l'attestation de conformité du rapport associé lors de la transmission [#4257]. Amélioration de la gestion et de la modification de l'attestation de conformité, notamment avec l'ajout d'un rapport associé [#4263, #4261, #4248].
- **Statistiques projets:** Ajout de la technologie aux exports lauréat et éliminés [#4323]. Ajout du producteur actuel dans la vue des statistiques projets [#4305].
- **Autocomplétion SIRET:** Autocomplétion du nom du producteur à partir du SIRET [#4266].
- **Notifications:** Ajout d'une notification lors de la modification de l'achèvement [#4252].

### Évolutions techniques
- **Refactoring:** Simplification des readable streams [#4321]. Simplification du formulaire représentant légal [#4308].
- **Sécurité:** Mise à jour de la librairie `shell-quote` pour corriger une vulnérabilité de sécurité [#4324]. Réécriture du mécanisme anti-CSRF [#4246].
- **Infrastructure:** Mise à jour de `better-auth` en version 1.6.11 [#4284]. Mise à jour de Next.js [#4242].
- **Outils:** Utilisation de Biome en remplacement de ESLint et Prettier pour le linting et le formattage du code [#4245].
- **Base de données:** Suppression des schémas et extensions PostgreSQL inutiles [#4294]. Correction des scripts de base de données [#4306].
- **CI/CD:** Amélioration de la gestion des SHA1 des actions GitHub pour le déploiement [#4310, #4300, #4273].

### Autres changements
- **Documentation:** Amélioration de la documentation et correction de typos [#4277, #4276].
- **Nettoyage de code:** Suppression de références inutiles dans le package lock [#4250]. Suppression du dossier `.vscode` du dépôt git [#4253].
- **Corrections de bugs:** Correction de divers bugs et flaky tests [#4335, #4328, #4319, #4318, #4283, #4281, #4275, #4268, #4265, #4259, #4255].
- **Import DN:** Ajout des types de fournisseur pour l'importation de données via DN [#4290].
- **Gestion des erreurs:** Correction de l'affichage des erreurs et amélioration de la gestion des erreurs dans les formulaires [#4326, #4286].
